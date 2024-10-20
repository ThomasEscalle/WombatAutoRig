from wombatAutoRig.src.core import FileHelper

### The TemplateManager class is responsible for managing the templates of the application.
class TemplateManager:

    def __init__(self):
        pass

    # Get the list of all the templates installed in the templates folder
    # This returns an array of arrays, where each array contains the name of the template and the path to the template
    def getTemplates(self):
        # Get the path of the templates folder
        templatePath = FileHelper.getTemplatesPath()

        # Get the list of all the folders in the templates folder
        templates = FileHelper.getAllFoldersInFolder(templatePath)

        # Create an array to store the templates
        templatesArray = []

        # Loop through all the folders
        for template in templates:
            # if the template is a "__pycache__" folder, skip it
            if template.find("__pycache__") != -1:
                continue

            template = template.replace("\\", "/")

            # Get the name of the template
            splitTemplate = template.split("/")
            templateName = splitTemplate[len(splitTemplate) - 1]

            # Get the path of the template
            templatePath = template

            # Add the template to the array
            templatesArray.append([templateName, templatePath])

        return templatesArray

    def getTemplate(self, templateName):
        # Get the path of the template
        templatePath = FileHelper.getTemplatesPath() + "/" + templateName


        # Get the path of the template main file
        templateMainPath = templatePath + "/template_main.py"

        print("Running template: " + templateMainPath)

        # Import the template main file
        templateMain = FileHelper.importFile(templateMainPath)

        # Run the main function of the template
        template = templateMain.Template()

        return template
    
