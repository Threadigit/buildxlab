import { cpSync, mkdirSync, rmSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
const output = fileURLToPath(new URL('../dist/', import.meta.url));
rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });
cpSync(fileURLToPath(new URL('../public/', import.meta.url)), output, { recursive: true });
console.log('Built static site in dist/');
