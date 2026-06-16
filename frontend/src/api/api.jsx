import axios from "axios";

// ✅ Production-safe API base URL
const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

// ---------------------------
// Extract Recipe API
// ---------------------------
export const extractRecipe = async (url) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/extract-recipe`, {
      url,
    });

    return response;
  } catch (error) {
    console.error("API Error:", error?.response?.data || error.message);
    throw error;
  }
};

// ---------------------------
// Get Recipes History (if you have endpoint)
// ---------------------------
export const getRecipes = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/recipes`);
    return response;
  } catch (error) {
    console.error("API Error:", error?.response?.data || error.message);
    throw error;
  }
};