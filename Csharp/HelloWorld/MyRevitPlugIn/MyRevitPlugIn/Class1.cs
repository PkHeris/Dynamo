using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Windows.Media.Imaging;
using Autodesk.Revit.Attributes;

namespace MyRevitPlugIn
{
    public class Class1 : IExternalApplication
    {
        public Result OnStartup(UIControlledApplication application)
        {
            try
            {
                RibbonPanel ribbonPanel = application.CreateRibbonPanel("PKH");

                // Create a button
                string thisAssemblyPath = Assembly.GetExecutingAssembly().Location;
                PushButtonData buttonData = new PushButtonData("cmdMyTest", "Greetings!", thisAssemblyPath, "MyRevitPlugIn.MyTest");
                PushButton pushButton = ribbonPanel.AddItem(buttonData) as PushButton;

                // Tool Tip
                pushButton.ToolTip = "Hello, This is Pooriya";
                Uri urlImage = new Uri(@"C:\Users\pheris\OneDrive - Modern Niagara Group\Desktop\revit\otter.png");
                BitmapImage bitmapImage = new BitmapImage(urlImage);
                pushButton.LargeImage = bitmapImage;
            }
            catch (Exception ex)
            {
                TaskDialog.Show("Error", "Failed to create the ribbon: " + ex.Message);
                return Result.Failed;
            }

            return Result.Succeeded;
        }

        public Result OnShutdown(UIControlledApplication application)
        {
            // Perform cleanup tasks if necessary
            return Result.Succeeded;
        }
    }

    [Transaction(TransactionMode.Manual)]
    public class MyTest : IExternalCommand
    {
        public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
        {
            var uiapp = commandData.Application;
            var uidoc = uiapp.ActiveUIDocument;

            TaskDialog.Show("Revit", "Hello, World!");

            return Result.Succeeded;
        }
    }
}
