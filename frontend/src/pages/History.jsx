import { useEffect, useState } from "react";
import { getRecipes, getRecipeById } from "../api/api";

export default function History() {
  const [recipes, setRecipes] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    load();
  }, []);

  const load = async () => {
    const res = await getRecipes();
    setRecipes(res.data);
  };

  const open = async (id) => {
    const res = await getRecipeById(id);
    setSelected(res.data);
  };

  return (
    <div className="space-y-4">

      {/* Table */}
      <div className="bg-white p-5 rounded-xl shadow">
        <h2 className="text-xl font-bold mb-4">Saved Recipes</h2>

        <table className="w-full text-left">
          <thead>
            <tr className="border-b">
              <th>Title</th>
              <th>Cuisine</th>
              <th>Difficulty</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            {recipes.map((r) => (
              <tr key={r.id} className="border-b">
                <td>{r.title}</td>
                <td>{r.cuisine}</td>
                <td>{r.difficulty}</td>
                <td>
                  <button
                    onClick={() => open(r.id)}
                    className="text-indigo-600"
                  >
                    View
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Modal */}
      {selected && (
        <div className="fixed inset-0 bg-black bg-opacity-40 flex justify-center items-center">
          <div className="bg-white p-6 rounded-xl w-[600px]">
            <h2 className="text-xl font-bold">{selected.title}</h2>

            <pre className="text-sm mt-3 bg-gray-100 p-3 rounded">
              {JSON.stringify(selected, null, 2)}
            </pre>

            <button
              onClick={() => setSelected(null)}
              className="mt-4 bg-red-500 text-white px-4 py-2 rounded"
            >
              Close
            </button>
          </div>
        </div>
      )}

    </div>
  );
}