import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: "../static/react",
    emptyOutDir: true,
    base: "./",
    server: {
      proxy: {
        "/api": "http://127.0.0.1:8000",
        "/media": "http://127.0.0.1:8000",
      },
    },
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
