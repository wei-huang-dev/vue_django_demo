import exportFromJSON from "export-from-json";

export const fileTypeParser = () => {
  function exportDataFromJSON(data, fileName, fileExportType) {

    if (!data) return;
    try {
      const exportType = exportFromJSON.types[fileExportType];
      exportFromJSON({ data, fileName, exportType });
    } catch (e) {
      throw new Error("Parsing failed!");
    }
  }

  return {
    exportDataFromJSON
  };
};