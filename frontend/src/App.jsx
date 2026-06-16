import { useState } from "react";
import ExtractRecipe from "./pages/ExtractRecipe";
import History from "./pages/History";

export default function App() {
  const [tab, setTab] = useState("extract");

  return (
    <div className="min-h-screen p-6">
      
      {/* Header */}
      <div className="bg-white shadow-md rounded-xl p-4 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-indigo-600">
          🍽️ Recipe Extractor AI
        </h1>

        <div className="space-x-2">
          <button
            onClick={() => setTab("extract")}
            className={`px-4 py-2 rounded-lg ${
              tab === "extract"
                ? "bg-indigo-600 text-white"
                : "bg-gray-200"
            }`}
          >
            Extract
          </button>

          <button
            onClick={() => setTab("history")}
            className={`px-4 py-2 rounded-lg ${
              tab === "history"
                ? "bg-indigo-600 text-white"
                : "bg-gray-200"
            }`}
          >
            History
          </button>
        </div>
      </div>

      {/* Content */}
      <div className="mt-6">
        {tab === "extract" ? <ExtractRecipe /> : <History />}
      </div>
    </div>
  );
}