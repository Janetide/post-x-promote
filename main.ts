// Copy POST.json from the repository root to the output directory.
// Node 22. No network, no clock, no files outside the repository.
// Run: mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? ".";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(botDir, "POST.json"), join(outDir, "POST.json"));
