import { useState } from "react";
import { extractRecipe } from "../api/api";
import toast from "react-hot-toast";

export default function ExtractRecipe() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleExtract = async () => {
  if (!url) {
    toast.error("Please enter a URL");
    return;
  }

  setLoading(true);
  setError("");
  setData(null);

  try {
    const res = await extractRecipe(url);

    if (res.data?.detail) {
      throw new Error(res.data.detail);
    }

    setData(res.data);
    toast.success("Recipe extracted successfully!");
  } catch (err) {
    setError(err.message);
    toast.error("Failed to extract recipe");
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="space-y-6">

      {/* INPUT CARD */}
      <div className="bg-white p-6 rounded-xl shadow">

        <input
          className="w-full border p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="Paste recipe URL..."
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button
          onClick={handleExtract}
          disabled={loading}
          className="mt-4 bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-lg disabled:opacity-50"
        >
          {loading ? "Extracting..." : "Extract Recipe"}
        </button>

        {/* ERROR MESSAGE */}
        {error && (
          <div className="mt-3 text-red-600 bg-red-100 p-2 rounded">
            {error}
          </div>
        )}
      </div>

      {/* LOADING STATE */}
      {loading && (
        <div className="bg-white p-6 rounded-xl shadow text-gray-500">
          Extracting recipe... please wait 🍳
        </div>
      )}

      {/* RESULT */}
      {data && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

          {/* RECIPE INFO */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h2 className="text-xl font-bold text-indigo-600">
              {data.recipe?.name || "No Title Found"}
            </h2>

            <h3 className="mt-3 font-semibold">Ingredients</h3>
            <ul className="list-disc ml-5">
              {(data.recipe?.ingredients || []).length > 0 ? (
                data.recipe.ingredients.map((i, idx) => (
                  <li key={idx}>{i}</li>
                ))
              ) : (
                <li>No ingredients found</li>
              )}
            </ul>
          </div>

          {/* INSTRUCTIONS */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h3 className="font-semibold text-lg">Instructions</h3>
            <ol className="list-decimal ml-5 space-y-2">
              {(data.recipe?.instructions || []).length > 0 ? (
                data.recipe.instructions.map((i, idx) => (
                  <li key={idx}>{i}</li>
                ))
              ) : (
                <li>No instructions found</li>
              )}
            </ol>
          </div>

          {/* NUTRITION */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h3 className="font-semibold">Nutrition</h3>
            <pre className="text-sm bg-gray-50 p-2 rounded">
              {JSON.stringify(data.generated?.nutrition || {}, null, 2)}
            </pre>
          </div>

          {/* SUBSTITUTIONS */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h3 className="font-semibold">Substitutions</h3>
            <ul className="list-disc ml-5">
              {(data.generated?.substitutions || []).length > 0 ? (
                data.generated.substitutions.map((s, i) => (
                  <li key={i}>{s}</li>
                ))
              ) : (
                <li>No substitutions found</li>
              )}
            </ul>
          </div>

          {/* SHOPPING LIST */}
          <div className="bg-white p-5 rounded-xl shadow md:col-span-2">
            <h3 className="font-semibold">Shopping List</h3>
            <pre className="text-sm bg-gray-50 p-2 rounded">
              {JSON.stringify(data.generated?.shopping_list || {}, null, 2)}
            </pre>
          </div>

          {/* RELATED RECIPES */}
          <div className="bg-white p-5 rounded-xl shadow md:col-span-2">
            <h3 className="font-semibold">Related Recipes</h3>
            <ul className="list-disc ml-5">
              {(data.generated?.related_recipes || []).length > 0 ? (
                data.generated.related_recipes.map((r, i) => (
                  <li key={i}>{r}</li>
                ))
              ) : (
                <li>No related recipes found</li>
              )}
            </ul>
          </div>

        </div>
      )}
    </div>
  );
}