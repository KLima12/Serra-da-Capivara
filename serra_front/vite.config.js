import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: "../templates/static/react",
    emptyOutDir: true,
    base: "./",
    rollupOptions: {
      output: {
        entryFileNames: "index.js",
        chunkFileNames: "index.js",
        assetFileNames: ({ name }) => {
          if (name && name.endsWith(".css")) {
            return "index.css";
          }
          return "[name].[ext]";
        },
      },
    },
  },
});
