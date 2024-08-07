using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System;
using System.Reflection;
using System.Windows.Media.Imaging;

namespace MyRevitCommand
{
    [Transaction(TransactionMode.Manual)]
    public class AutomationRibbon : IExternalApplication
    {
        public Result OnStartup(UIControlledApplication application)
        {
            // Define the ribbon tab name
            string tabName = "Automation Group";

            // Create the ribbon tab
            try
            {
                application.CreateRibbonTab(tabName);
            }
            catch (Exception ex)
            {
                // If the tab already exists, ignore the exception
                TaskDialog.Show("Error", ex.Message);
            }

            // Define the ribbon panel name
            string panelName = "Spool Package";

            // Create a ribbon panel
            RibbonPanel panel = application.CreateRibbonPanel(tabName, panelName);

            // Create buttons
            AddPushButton(panel, "CreateAssembly", "Create Assembly", "CreateAssembly.png", "MyRevitCommand.CreateAssemblyCommand", "This command creates an assembly.");
            AddPushButton(panel, "CreateSheetAndSchedules", "Create Sheet and Schedules", "CreateSheetAndSchedules.png", "MyRevitCommand.CreateSheetAndSchedulesCommand", "This command creates a sheet and schedules.");
            AddPushButton(panel, "MakeSubmissionPackage", "Make Submission Package", "MakeSubmissionPackage.png", "MyRevitCommand.MakeSubmissionPackageCommand", "This command makes a submission package.");
            AddPushButton(panel, "CreateWeldMap", "Create Weld Map", "CreateWeldMap.png", "MyRevitCommand.CreateWeldMapCommand", "This command creates a weld map.");
            AddPushButton(panel, "SuggestFieldWelds", "Suggest Field Welds", "SuggestFieldWelds.png", "MyRevitCommand.SuggestFieldWeldsCommand", "This command suggests field welds.");

            return Result.Succeeded;
        }

        private void AddPushButton(RibbonPanel panel, string name, string text, string imagePath, string commandNamespace, string toolTip)
        {
            string thisAssemblyPath = Assembly.GetExecutingAssembly().Location;
            PushButtonData buttonData = new PushButtonData(name, text, thisAssemblyPath, commandNamespace);
            PushButton pushButton = panel.AddItem(buttonData) as PushButton;

            // Set the button properties
            pushButton.ToolTip = toolTip;

            // Set the icon for the button from a local file path
            try
            {
                Uri iconUri = new Uri($@"YourDirectory}", UriKind.Absolute);
                BitmapImage iconImage = new BitmapImage();
                iconImage.BeginInit();
                iconImage.UriSource = iconUri;
                iconImage.DecodePixelWidth = 32;  // Set the width of the image to fit the button
                iconImage.DecodePixelHeight = 32; // Set the height of the image to fit the button
                iconImage.CacheOption = BitmapCacheOption.OnLoad;  // Ensure the image is fully loaded
                iconImage.EndInit();

                pushButton.LargeImage = iconImage;
            }
            catch (Exception ex)
            {
                TaskDialog.Show("Error", "Failed to load the image: " + ex.Message);
            }
        }

        public Result OnShutdown(UIControlledApplication application)
        {
            // Perform any clean-up operations
            return Result.Succeeded;
        }
    }

    // Define the external command classes
    [Transaction(TransactionMode.Manual)]
    public class CreateAssemblyCommand : IExternalCommand
    {
        public Result Execute(
          ExternalCommandData commandData,
          ref string message,
          ElementSet elements)
        {
            TaskDialog.Show("Create Assembly", "Create Assembly command executed successfully.");
            return Result.Succeeded;
        }
    }

    [Transaction(TransactionMode.Manual)]
    public class CreateSheetAndSchedulesCommand : IExternalCommand
    {
        public Result Execute(
          ExternalCommandData commandData,
          ref string message,
          ElementSet elements)
        {
            TaskDialog.Show("Create Sheet and Schedules", "Create Sheet and Schedules command executed successfully.");
            return Result.Succeeded;
        }
    }

    [Transaction(TransactionMode.Manual)]
    public class MakeSubmissionPackageCommand : IExternalCommand
    {
        public Result Execute(
          ExternalCommandData commandData,
          ref string message,
          ElementSet elements)
        {
            TaskDialog.Show("Make Submission Package", "Make Submission Package command executed successfully.");
            return Result.Succeeded;
        }
    }

    [Transaction(TransactionMode.Manual)]
    public class CreateWeldMapCommand : IExternalCommand
    {
        public Result Execute(
          ExternalCommandData commandData,
          ref string message,
          ElementSet elements)
        {
            TaskDialog.Show("Create Weld Map", "Create Weld Map command executed successfully.");
            return Result.Succeeded;
        }
    }

    [Transaction(TransactionMode.Manual)]
    public class SuggestFieldWeldsCommand : IExternalCommand
    {
        public Result Execute(
          ExternalCommandData commandData,
          ref string message,
          ElementSet elements)
        {
            TaskDialog.Show("Suggest Field Welds", "Suggest Field Welds command executed successfully.");
            return Result.Succeeded;
        }
    }
}
