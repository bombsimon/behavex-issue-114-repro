# `behavex` repro

Reproducible example for issue
[#114](https://github.com/hrcorval/behavex/issues/114).

By running `behave` or `behavex` with a single process the runner completes and
exit the test. By using more than once process pool, `behavex` will hang
forever.

## Running

### `behave`

```sh
› poetry run behave && echo "Exited"
Feature: Reproducible example of hanging test # features/example.feature:1

  Scenario: Run a non hanging test  # features/example.feature:3
    Given we have behave installed  # features/steps/example_steps.py:6 0.000s
    When we run a test              # features/steps/example_steps.py:11 0.000s
    Then the test is completed      # features/steps/example_steps.py:16 0.000s

  Scenario: Run a hanging test     # features/example.feature:8
    Given we run a test that exits # features/steps/example_steps.py:22
Exited
```

### `behavex` with a single process (no pool)

```sh
› poetry run behavex --parallel-processes 1 && echo "Exited"
|--------------------| ------------------------------------------------------------|
|ENV. VARIABLE       | VALUE                                                       |
|--------------------| ------------------------------------------------------------|
|HOME                | /Users/simon                                                |
|CONFIG              | /Users/simon/.../behavex/conf_behavex.cfg                   |
|OUTPUT              | /Users/simon/.../behavex-repro/output                       |
|TAGS                | None                                                        |
|PARALLEL_SCHEME     | scenario                                                    |
|PARALLEL_PROCESSES  | 1                                                           |
|FEATURES_PATH       | /Users/simon/.../behavex-repro/features                     |
|TEMP                | /Users/simon/.../behavex-repro/output/temp                  |
|LOGS                | /Users/simon/.../behavex-repro/output/outputs/logs          |
|LOGGING_LEVEL       | INFO                                                        |
|--------------------| ------------------------------------------------------------|
Exited
```

### `behavex` with more than one process

```sh
› poetry run behavex --parallel-processes 2 && echo "Exited"
|--------------------| ------------------------------------------------------------|
|ENV. VARIABLE       | VALUE                                                       |
|--------------------| ------------------------------------------------------------|
|HOME                | /Users/simon                                                |
|CONFIG              | /Users/simon/.../behavex/conf_behavex.cfg                   |
|OUTPUT              | /Users/simon/.../behavex-repro/output                       |
|TAGS                | None                                                        |
|PARALLEL_SCHEME     | scenario                                                    |
|PARALLEL_PROCESSES  | 2                                                           |
|FEATURES_PATH       | /Users/simon/.../behavex-repro/features                     |
|TEMP                | /Users/simon/.../behavex-repro/output/temp                  |
|LOGS                | /Users/simon/.../behavex-repro/output/outputs/logs          |
|LOGGING_LEVEL       | INFO                                                        |
|--------------------| ------------------------------------------------------------|
************************************************************
Running parallel scenarios

************************************************************
[HANGS]
```
