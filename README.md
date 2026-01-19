# test_repo_2

```mermaid
classDiagram
    %% Основные конфигурационные классы
    class ConfigManager {
        -args
        -config: Settings
        +__init__(args)
        +_get_config_path() str
        +_apply_cli_args_to_config_data(dict, args) dict
        +_process_config_data(dict) dict
        +get_model_settings(task_type: str) ModelSettings
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

    class WorkflowSettings {
        -generate_workflows: bool
        -include_tests: bool
        -include_black: bool
        -include_pep8: bool
        -include_autopep8: bool
        -include_fix_pep8: bool
        -include_pypi: bool
        -python_versions: List[str]
        -pep8_tool: Literal["flake8", "pylint"]
        -use_poetry: bool
        -branches: List[str]
        -codecov_token: bool
        -include_codecov: bool
    }

    %% Абстрактный класс ModelHandler и его реализации
    class ModelHandler {
        <<abstract>>
        -url: str
        -payload: dict
        +send_request(prompt: str, system_message: str) str
        +send_and_parse(prompt: str, parser: callable, system_message: str, retry_delay: float)
        +async_request(prompt: str, system_message: str) str
        +async_send_and_parse(prompt: str, parser: callable, system_message: str, retry_delay: float)
        +generate_concurrently(prompts: list[str], system_message: str) list
        +run_chain(prompt: str, parser: PydanticOutputParser, system_message: str, retry_delay: float) Any
        +async_run_chain(prompt: str, parser: PydanticOutputParser, system_message: str, retry_delay: float) Any
        +initialize_payload(model_settings: ModelSettings, prompt: str, system_message: str)
    }

    class ProtollmHandler {
        -model_settings: ModelSettings
        -max_retries: int
        -client
        +__init__(model_settings: ModelSettings)
        +send_request(prompt: str, system_message: str) str
        +send_and_parse(prompt: str, parser: callable, system_message: str, retry_delay: float)
        +async_request(prompt: str, system_message: str) str
        +async_send_and_parse(prompt: str, parser: callable, system_message: str, retry_delay: float)
        +generate_concurrently(prompts: list[str], system_message: str) list[str]
        +run_chain(prompt: str, parser: PydanticOutputParser, system_message: str, retry_delay: float) Any
        +async_run_chain(prompt: str, parser: PydanticOutputParser, system_message: str, retry_delay: float) Any
        -_build_model_url() str
        -_get_llm_params() dict
        -_configure_api(api: str, model_name: str)
        -_limit_tokens(text: str, safety_buffer: int, mode: str) str
    }

    class ModelHandlerFactory {
        +build(model_settings: ModelSettings) ProtollmHandler
    }

    class PayloadFactory {
        -job_id: str
        -temperature: float
        -tokens_limit: int
        -context_window: int
        -system_message: str
        -prompt: str
        -roles: list
        +__init__(model_settings: ModelSettings, prompt: str, system_message: str)
        +to_payload_completions() dict
    }

    %% Классы для планирования и оркестрации
    class ModeScheduler {
        -mode: str
        -args
        -config_manager: ConfigManager
        -model_settings: ModelSettings
        -sourcerank: SourceRank
        -workflow_manager: WorkflowManager
        -model_handler: ModelHandler
        -repo_url: str
        -metadata: RepositoryMetadata
        -base_path: str
        -prompts: PromptLoader
        -plan: dict
        +__init__(config_manager, sourcerank, args, workflow_manager, metadata)
        -_select_plan() dict
        -_basic_plan() dict
        -_make_request_for_auto_mode() dict
    }

    %% Классы для генерации докстрингов
    class DocGen {
        -config_manager: ConfigManager
        -model_settings: ModelSettings
        -model_handler: ProtollmHandler
        -main_idea: str
        +__init__(config_manager: ConfigManager)
        +format_structure_openai(structure: dict) str
        +format_structure_openai_short(filename: str, structure: dict) str
        +count_tokens(prompt: str) int
        +generate_class_documentation(class_details: list, semaphore: asyncio.Semaphore) str
        +update_class_documentation(class_details: list, semaphore: asyncio.Semaphore) str
        +generate_method_documentation(method_details: dict, semaphore: asyncio.Semaphore, context_code: str) str
        +update_method_documentation(method_details: dict, semaphore: asyncio.Semaphore, context_code: str, class_name: str) str
        +extract_pure_docstring(gpt_response: str) str
        +strip_docstring_from_body(body: str) str
        +insert_docstring_in_code(source_code: str, method_details: dict, generated_docstring: str, class_method: bool) str
        +insert_cls_docstring_in_code(source_code: str, class_name: str, generated_docstring: str) str
        +context_extractor(method_details: dict, structure: dict) str
        +format_with_black(filename: str)
        +_run_in_executor(parsed_structure: dict, project_source_code: dict, generated_docstrings: dict, n_workers: int) list[dict]
        +_perform_code_augmentations(args) dict[str, str]
        +_generate_docstrings_for_items(parsed_structure: dict, docstring_type: tuple | str, rate_limit: int) dict[str, dict]
        +_get_project_source_code(parsed_structure: dict, sem: asyncio.Semaphore) dict[str, str]
        +_write_augmented_code(parsed_structure: dict, augmented_code: list[dict], sem: asyncio.Semaphore)
        +_fetch_docstrings(file: str, file_meta: dict, project: dict, semaphore: asyncio.Semaphore) dict[str, list]
        +_fetch_docstrings_for_class(file: str, file_meta: dict, semaphore: asyncio.Semaphore) dict[str, list]
        +generate_the_main_idea(parsed_structure: dict, top_n: int)
        +summarize_submodules(project_structure, rate_limit: int) Dict[str, str]
        +convert_path_to_dot_notation(path) str
        +generate_documentation_mkdocs(path: str, files_info, modules_info)
        +create_mkdocs_git_workflow(repository_url: str, path: str)
        +_sanitize_name(name: str) str
        +_rename_invalid_dirs(repo_path: Path)
        +_add_init_files(repo_path: Path)
        +_purge_temp_files(path: str)
    }

    class OSA_TreeSitter {
        -cwd: str
        -import_map: dict
        -ignore_list: list[str]
        +__init__(scripts_path: str, ignore_list: list[str])
        +files_list(path: str) tuple[list, int] | tuple[list[str], int]
        -_is_ignored(path: Path) bool
        +_if_file_handler(path: str) str
        +open_file(file: str) str
        -_parser_build(filename: str) Parser
        -_parse_source_code(filename: str) tuple[tree_sitter.Tree, str]
        -_traverse_expression(class_attributes: list, expr_node: tree_sitter.Node) list
        -_get_attributes(class_attributes: list, block_node: tree_sitter.Node) list
        -_class_parser(structure: dict[dict, list], source_code: str, node: tree_sitter.Node, dec_list: list) list
        -_function_parser(structure: dict[dict, list], source_code: str, node: tree_sitter.Node, dec_list: list) list
        -_get_decorators(dec_list: list, dec_node: tree_sitter.Node) list
        -_resolve_import_path(import_text: str) dict
        -_extract_imports(root_node: tree_sitter.Node) dict
        -_resolve_import(call_text: str, call_alias: str, imports: dict, incantations: dict) dict
        -_resolve_method_calls(function_node: tree_sitter.Node, source_code: str, imports: dict) list
        +extract_structure(filename: str) list
        -_get_docstring(block_node: tree_sitter.Node) str
        -_traverse_block(block_node: tree_sitter.Node, source_code: bytes, imports: dict) list
        -_extract_function_details(function_node: tree_sitter.Node, source_code: str, imports: dict, dec_list: list) dict
        +analyze_directory(path: str) dict
        +show_results(results: dict)
        +log_results(results: dict)
    }

    %% Классы для работы с Git
    class GitAgent {
        <<abstract>>
    }

    class GitHubAgent {
        +__init__(repository: str, branch: str, author: str)
        +star_repository()
        +create_fork()
        +clone_repository()
        +create_and_checkout_branch()
        +upload_report(filename: str, output_path: str)
        +commit_and_push_changes(force: bool) dict
        +create_pull_request(body: str, changes: dict)
        +update_about_section(content: str)
    }

    class GitLabAgent {
        +__init__(repository: str, branch: str, author: str)
    }

    class GitverseAgent {
        +__init__(repository: str, branch: str, author: str)
    }

    %% Классы для управления workflow
    class WorkflowManager {
        <<abstract>>
    }

    class GitHubWorkflowManager {
        +__init__(repository: str, metadata: RepositoryMetadata, args)
        +update_workflow_config(config_manager: ConfigManager, plan: dict)
        +generate_workflow(config_manager: ConfigManager)
        +build_actual_plan(sourcerank: SourceRank) dict
    }

    class GitLabWorkflowManager {
        +__init__(repository: str, metadata: RepositoryMetadata, args)
    }

    class GitverseWorkflowManager {
        +__init__(repository: str, metadata: RepositoryMetadata, args)
    }

    %% Дополнительные классы
    class SourceRank {
        +__init__(config_manager: ConfigManager)
        +requirements_presence() bool
        +license_presence() bool
        -tree: str
    }

    class RepositoryMetadata {
        -description: str
    }

    class PromptLoader {
        +get(template_name: str) str
    }

    class ToDoList {
        +__init__(plan: dict)
        +mark_did(task: str)
        -list_for_report: list
    }

    %% Основные связи между классами
    ConfigManager --> Settings : создает и управляет
    Settings --> GitSettings : содержит
    Settings --> ModelGroupSettings : содержит
    Settings --> WorkflowSettings : содержит
    Settings --> PromptLoader : содержит
    
    ModelGroupSettings --> ModelSettings : содержит несколько
    
    ModeScheduler --> ConfigManager : использует
    ModeScheduler --> ModelHandler : использует
    ModeScheduler --> SourceRank : использует
    ModeScheduler --> WorkflowManager : использует
    
    ProtollmHandler --> ModelSettings : использует
    ProtollmHandler --|> ModelHandler : реализует
    
    ModelHandlerFactory --> ProtollmHandler : создает
    
    ProtollmHandler --> PayloadFactory : использует
    
    %% Связи для системы генерации докстрингов
    DocGen --> ConfigManager : использует
    DocGen --> ProtollmHandler : использует
    DocGen --> ModelHandlerFactory : создает обработчик
    
    DocGen ..> OSA_TreeSitter : анализирует структуру кода
