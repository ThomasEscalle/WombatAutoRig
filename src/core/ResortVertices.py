import maya.cmds as cmds

def get_ordered_vertices(Vertices, firstVertex):
    vertices = Vertices
    if not vertices:
        cmds.warning("Please select some vertices.")
        return []

    vertex_connections = {}  # Dictionary mapping vertices to their connected vertices

    # Step 1: Build a dictionary of connected vertices
    for v in vertices:
        connected_edges = cmds.polyListComponentConversion(v, toEdge=True)
        connected_edges = cmds.ls(connected_edges, fl=True)

        connected_vertices = set()
        for edge in connected_edges:
            verts = cmds.polyListComponentConversion(edge, toVertex=True)
            verts = cmds.ls(verts, fl=True)
            for vert in verts:
                if vert != v and vert in vertices:  # Avoid adding itself
                    connected_vertices.add(vert)

        vertex_connections[v] = list(connected_vertices)

    # Step 2: Start ordering the vertices
    sorted_vertices = [firstVertex]  # Start with the first selected vertex
    used_vertices = set(sorted_vertices)

    while len(sorted_vertices) < len(vertices):
        last_vertex = sorted_vertices[-1]  # Get the most recent vertex

        next_vertex = None
        for v in vertex_connections[last_vertex]:  # Look at connected vertices
            if v not in used_vertices:  # Find an unused vertex
                next_vertex = v
                break

        if next_vertex:
            sorted_vertices.append(next_vertex)  # Add to the ordered list
            used_vertices.add(next_vertex)  # Mark as used
        else:
            break  # Stop if no more connected vertices are found

    return sorted_vertices

