# test_repo_2

```mermaid
classDiagram
    %% ==================== МОДУЛЬ КОНФИГУРАЦИИ ====================
    class ConfigManager {
        -args: argparse.Namespace
        -config: Settings
        +__init__(args)
        +get_model_settings(task_type) ModelSettings
        +get_git_settings() GitSettings
    }

    class Settings {
        +git: GitSettings
        +llm: ModelGroupSettings
        +workflows: WorkflowSettings
    }

    class GitSettings {
        +repository: Path | str
        +full_name: str
        +host: str
        +name: str
    }

    class ModelSettings {
        +api: str
        +rate_limit: PositiveInt
        +base_url: str
        +model: str
        +temperature: NonNegativeFloat
        +max_tokens: PositiveInt
        +context_window: PositiveInt
        +max_retries: PositiveInt
        +system_prompt: str
    }

    class ModelGroupSettings {
        +default: ModelSettings
        +for_docstring_gen: ModelSettings
    }

    %% ==================== МОДУЛЬ МОДЕЛЕЙ LLM ====================
    class ModelHandler {
        <<abstract>>
        +send_request(prompt, system_message) str*
        +async_request(prompt, system_message) str*
        +generate_concurrently(prompts, system_message) list*
    }

    class ProtollmHandler {
        -model_settings: ModelSettings
        -client
        +__init__(model_settings)
        +send_request(prompt, system_message) str
        +async_request(prompt, system_message) str
        +generate_concurrently(prompts, system_message) list
        -_limit_tokens(text) str
    }

    class ModelHandlerFactory {
        <<static>>
        +build(model_settings) ProtollmHandler
    }

    %% ==================== МОДУЛЬ АНАЛИЗА КОДА ====================
    class OSA_TreeSitter {
        -cwd: str
        -ignore_list: list[str]
        +__init__(scripts_path, ignore_list)
        +analyze_directory(path) dict
        +extract_structure(filename) dict
    }

    %% ==================== МОДУЛЬ ГЕНЕРАЦИИ ДОКСТРИНГОВ ====================
    class DocGen {
        -config_manager: ConfigManager
        -model_handler: ProtollmHandler
        -main_idea: str
        
        +__init__(config_manager)
        +generate_class_documentation(class_details, semaphore) str
        +generate_method_documentation(method_details, semaphore) str
        +extract_pure_docstring(gpt_response) str
        +insert_docstring_in_code(source_code, method_details, docstring) str
        +insert_cls_docstring_in_code(source_code, class_name, docstring) str
        +_run_in_executor(parsed_structure, source_code, docstrings, n_workers) list
        +_generate_docstrings_for_items(parsed_structure, docstring_type, rate_limit) dict
        +generate_the_main_idea(parsed_structure)
        +generate_documentation_mkdocs(path, files_info, modules_info)
    }

    %% ==================== МОДУЛЬ ОРКЕСТРАЦИИ ====================
    class RunModule {
        +main()
        +generate_docstrings(config_manager, loop, ignore_list)
    }

    %% ==================== СВЯЗИ КОМПОЗИЦИИ ====================
    Settings *-- GitSettings
    Settings *-- ModelGroupSettings
    ModelGroupSettings *-- ModelSettings
    ConfigManager *-- Settings
    DocGen *-- ConfigManager
    DocGen *-- ProtollmHandler

    %% ==================== СВЯЗИ СОЗДАНИЯ ====================
    ConfigManager ..> Settings : creates
    ModelHandlerFactory ..> ProtollmHandler : creates
    RunModule ..> ConfigManager : creates
    RunModule ..> DocGen : creates
    DocGen ..> ModelHandlerFactory : uses
    DocGen ..> OSA_TreeSitter : uses

    %% ==================== НАСЛЕДОВАНИЕ ====================
    ModelHandler <|-- ProtollmHandler

    %% ==================== ЗАВИСИМОСТИ ====================
    ProtollmHandler ..> ModelSettings : requires
