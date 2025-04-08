import { fileURLToPath } from 'node:url';
import path from 'node:path';

import { fixupConfigRules, fixupPluginRules } from '@eslint/compat';
import typescriptEslint from '@typescript-eslint/eslint-plugin';
import unusedImports from 'eslint-plugin-unused-imports';
import perfectionist from 'eslint-plugin-perfectionist';
import tsParser from '@typescript-eslint/parser';
import { FlatCompat } from '@eslint/eslintrc';
import globals from 'globals';
import js from '@eslint/js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all
});

export default [
  ...fixupConfigRules(
    compat.extends(
      'plugin:@typescript-eslint/recommended',
      'eslint:recommended'
    )
  ),
  {
    plugins: {
      '@typescript-eslint': fixupPluginRules(typescriptEslint),
      'unused-imports': unusedImports,
      perfectionist
    },

    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node
      },

      parser: tsParser
    },

    rules: {
      '@typescript-eslint/no-empty-function': 'off',
      '@typescript-eslint/no-unused-vars': 'error',
      '@typescript-eslint/no-explicit-any': 'off',
      'unused-imports/no-unused-imports': 'error',
      'no-unused-vars': 'off',

      'perfectionist/sort-imports': [
        'error',
        {
          order: 'desc',
          environment: 'bun',
          type: 'line-length',
          newlinesBetween: 'always',
          groups: [
            'builtin',
            'external',
            'internal',
            'share',
            ['sibling', 'parent'],
            'index',
            'unknown'
          ],
          customGroups: {
            value: {
              share: ['^share']
            }
          }
        }
      ]
    }
  }
];
