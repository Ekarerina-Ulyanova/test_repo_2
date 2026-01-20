# test_repo_2

```mermaid
classDiagram
    %% Основные классы из settings.py
    class ConfigManager {
        -args
        -config: Settings
        +__init__(args)
        +_get_config_path() str
        +_apply_cli_args_to_config_data(config_data, args) dict
        +_process_config_data(config_data) dict
        +get_model_settings(task_type) ModelSettings
        +get_git_settings() GitSettings
        +get_workflow_settings() WorkflowSettings
        +get_prompts() PromptLoader
    }

    class Settings {
        -git: GitSettings
        -llm: ModelGroupSettings
        -workflows: WorkflowSettings
        -prompts: PromptLoader
    }

    class GitSettings {
        -repository: Path | str
        -full_name: str
        -host_domain: str
        -host: str
        -name: str
        +set_git_attributes()
    }

    class ModelSettings {
        -api: str
        -rate_limit: PositiveInt
        -base_url: str
        -encoder: str
        -host_name: AnyHttpUrl
        -localhost: AnyHttpUrl
        -model: str
        -path: str
        -temperature: NonNegativeFloat
        -max_tokens: PositiveInt
        -context_window: PositiveInt
        -top_p: NonNegativeFloat
        -max_retries: PositiveInt
        -allowed_providers: list[str]
        -system_prompt: str
    }

    class ModelGroupSettings {
        -default: ModelSettings
        -for_docstring_gen: ModelSettings
        -for_readme_gen: ModelSettings
        -for_validation: ModelSettings
        -for_general_tasks: ModelSettings
    }

    %% Основные классы из models.py
    class ModelHandler {
        <<abstract>>
        #url: str
        #payload: dict
        +send_request(prompt, system_message) str*
        +send_and_parse(prompt, parser, system_message, retry_delay)*
        +async_request(prompt, system_message) str*
        +async_send_and_parse(prompt, parser, system_message, retry_delay)*
        +generate_concurrently(prompts, system_message) list*
        +run_chain(prompt, parser, system_message, retry_delay) Any*
        +async_run_chain(prompt, parser, system_message, retry_delay) Any*
        +initialize_payload(model_settings, prompt, system_message)
    }

    class ProtollmHandler {
        -model_settings: ModelSettings
        -max_retries: int
        -client
        +__init__(model_settings)
        +send_request(prompt, system_message) str
        +send_and_parse(prompt, parser, system_message, retry_delay)
        +async_request(prompt, system_message) str
        +async_send_and_parse(prompt, parser, system_message, retry_delay)
        +generate_concurrently(prompts, system_message) list
        +run_chain(prompt, parser, system_message, retry_delay) Any
        +async_run_chain(prompt, parser, system_message, retry_delay) Any
        +_build_model_url() str
        +_get_llm_params() dict
        +_configure_api(api, model_name)
        +_limit_tokens(text, safety_buffer, mode) str
    }

    class PayloadFactory {
        -job_id: str
        -temperature: float
        -tokens_limit: int
        -context_window: int
        -system_message: str
        -prompt: str
        -roles: list
        +__init__(model_settings, prompt, system_message)
        +to_payload_completions() dict
    }

    class ModelHandlerFactory {
        +build(model_settings) ProtollmHandler
    }

    %% Основные классы из osa_treesitter.py
    class OSA_TreeSitter {
        -cwd: str
        -import_map: dict
        -ignore_list: list[str]
        +__init__(scripts_path, ignore_list)
        +files_list(path) tuple[list, int]
        -_is_ignored(path) bool
        -_if_file_handler(path) str
        +open_file(file) str
        -_parser_build(filename) Parser
        -_parse_source_code(filename) tuple
        -_traverse_expression(class_attributes, expr_node) list
        -_get_attributes(class_attributes, block_node) list
        -_class_parser(structure, source_code, node, dec_list) list
        -_function_parser(structure, source_code, node, dec_list) list
        -_get_decorators(dec_list, dec_node) list
        -_resolve_import_path(import_text) dict
        -_extract_imports(root_node) dict
        -_resolve_import(call_text, call_alias, imports, incantations) dict
        -_resolve_method_calls(function_node, source_code, imports) list
        +extract_structure(filename) list
        -_get_docstring(block_node) str
        -_traverse_block(block_node, source_code, imports) list
        -_extract_function_details(function_node, source_code, imports, dec_list) dict
        +analyze_directory(path) dict
        +show_results(results)
        +log_results(results)
    }

    %% Основные классы из docgen.py
    class DocGen {
        -config_manager: ConfigManager
        -model_settings: ModelSettings
        -model_handler: ProtollmHandler
        -main_idea: str
        +__init__(config_manager)
        +format_structure_openai(structure) str
        +format_structure_openai_short(filename, structure) str
        -_format_class(item) str
        -_format_method(method) str
        -_format_function(item) str
        -_format_class_short(item) str
        -_format_function_short(item) str
        +count_tokens(prompt) int
        +generate_class_documentation(class_details, semaphore) str
        +update_class_documentation(class_details, semaphore) str
        +generate_method_documentation(method_details, semaphore, context_code) str
        +update_method_documentation(method_details, semaphore, context_code, class_name) str
        +extract_pure_docstring(gpt_response) str
        +strip_docstring_from_body(body) str
        +insert_docstring_in_code(source_code, method_details, generated_docstring, class_method) str
        +insert_cls_docstring_in_code(source_code, class_name, generated_docstring) str
        +context_extractor(method_details, structure) str
        +format_with_black(filename)
        +_run_in_executor(parsed_structure, project_source_code, generated_docstrings, n_workers) list[dict]
        -_perform_code_augmentations(args) dict
        +_generate_docstrings_for_items(parsed_structure, docstring_type, rate_limit) dict
        +_get_project_source_code(parsed_structure, sem) dict
        +_write_augmented_code(parsed_structure, augmented_code, sem)
        -_fetch_docstrings(file, file_meta, project, semaphore) dict
        -_fetch_docstrings_for_class(file, file_meta, semaphore) dict
        +generate_the_main_idea(parsed_structure, top_n)
        +summarize_submodules(project_structure, rate_limit) dict
        -summarize_directory(name, file_summaries, submodule_summaries) str
        -traverse_and_summarize(path, project) str
        +convert_path_to_dot_notation(path) str
        +generate_documentation_mkdocs(path, files_info, modules_info)
        +create_mkdocs_git_workflow(repository_url, path)
        -_sanitize_name(name) str
        -_rename_invalid_dirs(repo_path)
        -_add_init_files(repo_path)
        +_purge_temp_files(path)
    }

    %% Основные классы из run.py
    class RunModule {
        +main()
        +initialize_git_platform(args) tuple[GitAgent, WorkflowManager]
        +convert_notebooks(repo_url, notebook_paths)
        +generate_requirements(repo_url)
        +generate_docstrings(config_manager, loop, ignore_list)
    }

    %% Связи наследования
    ModelHandler <|-- ProtollmHandler : implements

    %% Связи ассоциации (использование)
    RunModule --> ConfigManager : uses
    RunModule --> DocGen : creates
    RunModule --> OSA_TreeSitter : creates
    
    DocGen --> ConfigManager : depends on
    DocGen --> ProtollmHandler : uses
    DocGen --> ModelHandlerFactory : uses
    DocGen --> OSA_TreeSitter : uses
    
    ConfigManager --> Settings : creates
    ConfigManager --> ModelSettings : creates
    ConfigManager --> GitSettings : creates
    
    ProtollmHandler --> ModelSettings : depends on
    ProtollmHandler --> PayloadFactory : creates
    
    ModelHandlerFactory --> ProtollmHandler : creates
    
    OSA_TreeSitter --> tree_sitter.Parser : uses
    OSA_TreeSitter --> tree_sitter.Tree : creates
    
    %% Композиция/Агрегация
    Settings *-- GitSettings
    Settings *-- ModelGroupSettings
    Settings *-- WorkflowSettings
    ModelGroupSettings *-- ModelSettings
    
    %% Зависимости
    DocGen ..> asyncio.Semaphore : uses
    DocGen ..> aiofiles : uses
    DocGen ..> black : uses
    DocGen ..> tiktoken : uses
    
    DocGen ..> OSA_TreeSitter : анализирует структуру кода
