
DOMAIN_BLUEPRINTS = {

    "data_science": {
        "layers": {
            "language": ["Python", "R"],
            "data_handling": ["Pandas", "NumPy", "SciPy"],
            "ml": ["Scikit-learn", "XGBoost", "LightGBM"],
            "deep_learning": ["TensorFlow", "PyTorch", "Keras"],
            "visualization": ["Matplotlib", "Seaborn", "Plotly"],
            "database": ["SQL", "PostgreSQL", "MySQL"],
            "big_data": ["Apache Spark", "Hadoop"],
            "tools": ["Git", "Jupyter Notebook"]
        }
    },

    "ml_ai": {
        "layers": {
            "language": ["Python"],
            "ml_frameworks": ["TensorFlow", "PyTorch", "Keras"],
            "ml_libraries": ["Scikit-learn", "XGBoost", "LightGBM"],
            "nlp": ["NLTK", "spaCy", "Hugging Face"],
            "computer_vision": ["OpenCV"],
            "data": ["Pandas", "NumPy"],
            "deployment": ["Flask", "FastAPI", "Docker"],
            "tools": ["Git", "Jupyter Notebook"]
        }
    },

    "backend": {
        "layers": {
            "language": ["Python", "Java", "Go"],
            "framework": ["Django", "Flask", "Spring Boot", "Express.js", "FastAPI"],
            "database": ["PostgreSQL", "MySQL", "MongoDB", "Redis"],
            "api": ["REST API", "GraphQL"],
            "testing": ["Pytest", "JUnit"],
            "cloud": ["AWS", "Docker"],
            "tools": ["Git", "Postman"],
            "architecture": ["Microservices"]
        }
    },

    "frontend": {
        "layers": {
            "language": ["JavaScript", "TypeScript", "HTML", "CSS"],
            "framework": ["React", "Angular", "Vue.js", "Next.js"],
            "styling": ["Tailwind CSS", "Bootstrap", "Sass"],
            "state_management": ["Redux"],
            "testing": ["Jest", "Cypress"],
            "build_tools": ["Webpack"],
            "tools": ["Git"]
        }
    },

    "fullstack": {
        "layers": {
            "frontend": ["React", "Next.js", "Vue.js"],
            "backend": ["Node.js", "Express.js", "Django", "Flask"],
            "database": ["PostgreSQL", "MongoDB", "MySQL"],
            "api": ["REST API", "GraphQL"],
            "deployment": ["Docker", "AWS"],
            "tools": ["Git"],
            "architecture": ["Microservices"]
        }
    },

    "devops": {
        "layers": {
            "language": ["Python", "Shell Scripting"],
            "containerization": ["Docker", "Kubernetes"],
            "cloud": ["AWS", "Azure", "Google Cloud Platform"],
            "ci_cd": ["Jenkins", "GitHub Actions", "GitLab CI"],
            "infrastructure": ["Terraform", "Ansible"],
            "monitoring": ["Prometheus", "Grafana"],
            "version_control": ["Git"],
            "concepts": ["Linux"]
        }
    },

    "fintech": {
        "layers": {
            "language": ["Python"],
            "data": ["Pandas", "NumPy", "yfinance"],
            "trading": ["CCXT", "Alpaca", "Backtrader"],
            "ml": ["Scikit-learn", "XGBoost"],
            "visualization": ["Matplotlib", "Plotly"],
            "database": ["PostgreSQL"],
            "backend": ["Flask", "FastAPI"],
            "concepts": [
                "Technical Analysis",
                "Algorithmic Trading",
                "Portfolio Optimization",
                "Risk Management",
                "Monte Carlo Simulation"
            ],
            "tools": ["Git", "Jupyter Notebook"]
        }
    },

    "data_engineering": {
        "layers": {
            "language": ["Python", "SQL", "Scala"],
            "big_data": ["Apache Spark", "Hadoop", "Apache Kafka"],
            "databases": ["PostgreSQL", "Cassandra", "Snowflake"],
            "etl": ["Apache Airflow", "dbt"],
            "cloud": ["AWS", "Google Cloud Platform", "Azure"],
            "streaming": ["Apache Kafka"],
            "tools": ["Git", "Docker"],
            "concepts": ["Data Warehousing", "ETL"]
        }
    }
}
SKILL_DICT = {
    "programming_languages": {
        "python": {
            "canonical": "Python",
            "aliases": ["python", "py", "python3", "python2"],
            "category": "programming_language",
            "domain_relevance": ["data_science", "ml_ai", "backend", "automation", "fintech"]
        },
        "javascript": {
            "canonical": "JavaScript",
            "aliases": ["javascript", "js", "es6", "es7", "ecmascript"],
            "category": "programming_language",
            "domain_relevance": ["frontend", "backend", "fullstack", "web_dev"]
        },
        "java": {
            "canonical": "Java",
            "aliases": ["java", "java8", "java11", "java17", "jdk"],
            "category": "programming_language",
            "domain_relevance": ["backend", "android", "enterprise", "systems"]
        },
        "cpp": {
            "canonical": "C++",
            "aliases": ["c++", "cpp", "c plus plus", "cplusplus","c"],
            "category": "programming_language",
            "domain_relevance": ["systems", "game_dev", "competitive_programming", "embedded"]
        },
        "c_lang": {
            "canonical": "C",
            "aliases": ["c programming", "c language", "ansi c","c"],
            "category": "programming_language",
            "domain_relevance": ["systems", "embedded", "os_dev", "low_level"]
        },
        "typescript": {
            "canonical": "TypeScript",
            "aliases": ["typescript", "ts"],
            "category": "programming_language",
            "domain_relevance": ["frontend", "backend", "fullstack"]
        },
        "go": {
            "canonical": "Go",
            "aliases": ["golang", "go lang"],
            "category": "programming_language",
            "domain_relevance": ["backend", "cloud", "systems", "devops"]
        },
        "rust": {
            "canonical": "Rust",
            "aliases": ["rust", "rust-lang", "rustlang"],
            "category": "programming_language",
            "domain_relevance": ["systems", "blockchain", "performance"]
        },
        "kotlin": {
            "canonical": "Kotlin",
            "aliases": ["kotlin"],
            "category": "programming_language",
            "domain_relevance": ["android", "backend"]
        },
        "swift": {
            "canonical": "Swift",
            "aliases": ["swift"],
            "category": "programming_language",
            "domain_relevance": ["ios", "mobile"]
        },
        "php": {
            "canonical": "PHP",
            "aliases": ["php", "php7", "php8"],
            "category": "programming_language",
            "domain_relevance": ["backend", "web_dev"]
        },
        "ruby": {
            "canonical": "Ruby",
            "aliases": ["ruby"],
            "category": "programming_language",
            "domain_relevance": ["backend", "web_dev"]
        },
        "r_lang": {
            "canonical": "R",
            "aliases": ["r programming", "r language"],
            "category": "programming_language",
            "domain_relevance": ["data_science", "statistics", "ml_ai"]
        },
        "scala": {
            "canonical": "Scala",
            "aliases": ["scala"],
            "category": "programming_language",
            "domain_relevance": ["backend", "big_data", "data_engineering"]
        },
        "sql": {
            "canonical": "SQL",
            "aliases": ["sql", "structured query language", "t-sql", "pl/sql"],
            "category": "programming_language",
            "domain_relevance": ["data_science", "backend", "data_engineering", "analytics"]
        },
        "dart": {
            "canonical": "Dart",
            "aliases": ["dart"],
            "category": "programming_language",
            "domain_relevance": ["mobile", "frontend"]
        },
        "shell": {
            "canonical": "Shell Scripting",
            "aliases": ["bash", "shell scripting", "zsh", "powershell", "shell script"],
            "category": "programming_language",
            "domain_relevance": ["devops", "automation", "systems"]
        },
        "html": {
            "canonical": "HTML",
            "aliases": ["html", "html5"],
            "category": "markup_language",
            "domain_relevance": ["frontend", "web_dev"]
        },
        "css": {
            "canonical": "CSS",
            "aliases": ["css", "css3"],
            "category": "styling_language",
            "domain_relevance": ["frontend", "web_dev"]
        }
    },
    
    "frontend_frameworks": {
        "react": {
            "canonical": "React",
            "aliases": ["react", "reactjs", "react.js", "react js"],
            "category": "frontend_framework",
            "domain_relevance": ["frontend", "fullstack", "web_dev"]
        },
        "angular": {
            "canonical": "Angular",
            "aliases": ["angular", "angularjs", "angular2", "angular 2+", "angular 2"],
            "category": "frontend_framework",
            "domain_relevance": ["frontend", "fullstack", "web_dev"]
        },
        "vue": {
            "canonical": "Vue.js",
            "aliases": ["vue", "vuejs", "vue.js", "vue js"],
            "category": "frontend_framework",
            "domain_relevance": ["frontend", "fullstack", "web_dev"]
        },
        "nextjs": {
            "canonical": "Next.js",
            "aliases": ["next", "nextjs", "next.js", "next js"],
            "category": "frontend_framework",
            "domain_relevance": ["frontend", "fullstack", "web_dev"]
        },
        "svelte": {
            "canonical": "Svelte",
            "aliases": ["svelte", "sveltekit"],
            "category": "frontend_framework",
            "domain_relevance": ["frontend", "web_dev"]
        },
        "jquery": {
            "canonical": "jQuery",
            "aliases": ["jquery"],
            "category": "frontend_library",
            "domain_relevance": ["frontend", "web_dev"]
        },
        "bootstrap": {
            "canonical": "Bootstrap",
            "aliases": ["bootstrap", "bootstrap5", "bootstrap 5", "bootstrap4"],
            "category": "css_framework",
            "domain_relevance": ["frontend", "web_dev"]
        },
        "tailwind": {
            "canonical": "Tailwind CSS",
            "aliases": ["tailwind", "tailwindcss", "tailwind css"],
            "category": "css_framework",
            "domain_relevance": ["frontend", "web_dev"]
        },
        "materialui": {
            "canonical": "Material-UI",
            "aliases": ["material ui", "mui", "material-ui", "materialui"],
            "category": "ui_library",
            "domain_relevance": ["frontend", "web_dev"]
        },
        "redux": {
            "canonical": "Redux",
            "aliases": ["redux", "redux toolkit", "react-redux", "react redux"],
            "category": "state_management",
            "domain_relevance": ["frontend", "web_dev"]
        },
        "sass": {
            "canonical": "Sass",
            "aliases": ["sass", "scss"],
            "category": "css_preprocessor",
            "domain_relevance": ["frontend", "web_dev"]
        }
    },
    
    "backend_frameworks": {
        "nodejs": {
            "canonical": "Node.js",
            "aliases": ["node", "nodejs", "node.js", "node js"],
            "category": "backend_runtime",
            "domain_relevance": ["backend", "fullstack"]
        },
        "express": {
            "canonical": "Express.js",
            "aliases": ["express", "expressjs", "express.js"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "fullstack"]
        },
        "django": {
            "canonical": "Django",
            "aliases": ["django"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "fullstack", "web_dev"]
        },
        "flask": {
            "canonical": "Flask",
            "aliases": ["flask"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "fullstack", "web_dev", "ml_ai"]
        },
        "fastapi": {
            "canonical": "FastAPI",
            "aliases": ["fastapi", "fast api"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "ml_ai", "api_dev"]
        },
        "spring": {
            "canonical": "Spring Boot",
            "aliases": ["spring", "spring boot", "springboot", "spring framework"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "enterprise", "java_dev"]
        },
        "rails": {
            "canonical": "Ruby on Rails",
            "aliases": ["rails", "ruby on rails", "ror"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "web_dev"]
        },
        "laravel": {
            "canonical": "Laravel",
            "aliases": ["laravel"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "web_dev"]
        },
        "nestjs": {
            "canonical": "NestJS",
            "aliases": ["nest", "nestjs", "nest.js"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "fullstack"]
        },
        "aspnet": {
            "canonical": "ASP.NET",
            "aliases": ["asp.net", "aspnet", "asp net", ".net core", "dotnet"],
            "category": "backend_framework",
            "domain_relevance": ["backend", "enterprise"]
        }
    },
    
    "databases": {
        "mysql": {
            "canonical": "MySQL",
            "aliases": ["mysql"],
            "category": "relational_database",
            "domain_relevance": ["backend", "data_engineering", "fullstack"]
        },
        "postgresql": {
            "canonical": "PostgreSQL",
            "aliases": ["postgresql", "postgres", "psql"],
            "category": "relational_database",
            "domain_relevance": ["backend", "data_engineering", "fullstack"]
        },
        "mongodb": {
            "canonical": "MongoDB",
            "aliases": ["mongodb", "mongo"],
            "category": "nosql_database",
            "domain_relevance": ["backend", "fullstack"]
        },
        "redis": {
            "canonical": "Redis",
            "aliases": ["redis"],
            "category": "cache_database",
            "domain_relevance": ["backend", "systems", "performance"]
        },
        "sqlite": {
            "canonical": "SQLite",
            "aliases": ["sqlite", "sqlite3"],
            "category": "embedded_database",
            "domain_relevance": ["backend", "mobile", "embedded"]
        },
        "cassandra": {
            "canonical": "Cassandra",
            "aliases": ["cassandra", "apache cassandra"],
            "category": "nosql_database",
            "domain_relevance": ["big_data", "data_engineering"]
        },
        "dynamodb": {
            "canonical": "DynamoDB",
            "aliases": ["dynamodb", "dynamo db"],
            "category": "nosql_database",
            "domain_relevance": ["backend", "cloud", "aws"]
        },
        "firebase": {
            "canonical": "Firebase",
            "aliases": ["firebase", "firestore"],
            "category": "baas_database",
            "domain_relevance": ["mobile", "web_dev", "fullstack"]
        },
        "elasticsearch": {
            "canonical": "Elasticsearch",
            "aliases": ["elasticsearch", "elastic search"],
            "category": "search_database",
            "domain_relevance": ["backend", "data_engineering", "search"]
        },
        "oracle": {
            "canonical": "Oracle Database",
            "aliases": ["oracle", "oracle db", "oracle database"],
            "category": "relational_database",
            "domain_relevance": ["backend", "enterprise"]
        },
        "mssql": {
            "canonical": "Microsoft SQL Server",
            "aliases": ["mssql", "sql server", "microsoft sql server"],
            "category": "relational_database",
            "domain_relevance": ["backend", "enterprise"]
        }
    },
    
    "data_science_ml": {
        "pandas": {
            "canonical": "Pandas",
            "aliases": ["pandas", "pd"],
            "category": "data_manipulation",
            "domain_relevance": ["data_science", "ml_ai", "analytics", "fintech"]
        },
        "numpy": {
            "canonical": "NumPy",
            "aliases": ["numpy", "np"],
            "category": "numerical_computing",
            "domain_relevance": ["data_science", "ml_ai", "scientific_computing"]
        },
        "scikit-learn": {
            "canonical": "Scikit-learn",
            "aliases": ["scikit-learn", "sklearn", "scikit learn"],
            "category": "machine_learning",
            "domain_relevance": ["ml_ai", "data_science"]
        },
        "tensorflow": {
            "canonical": "TensorFlow",
            "aliases": ["tensorflow", "tf", "tensor flow"],
            "category": "deep_learning",
            "domain_relevance": ["ml_ai", "deep_learning", "ai"]
        },
        "pytorch": {
            "canonical": "PyTorch",
            "aliases": ["pytorch", "torch"],
            "category": "deep_learning",
            "domain_relevance": ["ml_ai", "deep_learning", "ai"]
        },
        "keras": {
            "canonical": "Keras",
            "aliases": ["keras"],
            "category": "deep_learning",
            "domain_relevance": ["ml_ai", "deep_learning"]
        },
        "matplotlib": {
            "canonical": "Matplotlib",
            "aliases": ["matplotlib", "pyplot"],
            "category": "data_visualization",
            "domain_relevance": ["data_science", "analytics"]
        },
        "seaborn": {
            "canonical": "Seaborn",
            "aliases": ["seaborn", "sns"],
            "category": "data_visualization",
            "domain_relevance": ["data_science", "analytics"]
        },
        "plotly": {
            "canonical": "Plotly",
            "aliases": ["plotly"],
            "category": "data_visualization",
            "domain_relevance": ["data_science", "analytics"]
        },
        "opencv": {
            "canonical": "OpenCV",
            "aliases": ["opencv", "cv2", "open cv"],
            "category": "computer_vision",
            "domain_relevance": ["ml_ai", "computer_vision"]
        },
        "nltk": {
            "canonical": "NLTK",
            "aliases": ["nltk", "natural language toolkit"],
            "category": "nlp",
            "domain_relevance": ["ml_ai", "nlp"]
        },
        "spacy": {
            "canonical": "spaCy",
            "aliases": ["spacy", "spa cy"],
            "category": "nlp",
            "domain_relevance": ["ml_ai", "nlp"]
        },
        "huggingface": {
            "canonical": "Hugging Face",
            "aliases": ["huggingface", "hugging face", "transformers", "hf"],
            "category": "nlp",
            "domain_relevance": ["ml_ai", "nlp", "llm"]
        },
        "xgboost": {
            "canonical": "XGBoost",
            "aliases": ["xgboost", "xgb"],
            "category": "machine_learning",
            "domain_relevance": ["ml_ai", "data_science"]
        },
        "lightgbm": {
            "canonical": "LightGBM",
            "aliases": ["lightgbm", "lgbm", "light gbm"],
            "category": "machine_learning",
            "domain_relevance": ["ml_ai", "data_science"]
        },
        "jupyter": {
            "canonical": "Jupyter Notebook",
            "aliases": ["jupyter", "jupyter notebook", "ipynb"],
            "category": "development_tool",
            "domain_relevance": ["data_science", "ml_ai", "research"]
        },
        "scipy": {
            "canonical": "SciPy",
            "aliases": ["scipy"],
            "category": "scientific_computing",
            "domain_relevance": ["data_science", "scientific_computing"]
        },
        "statsmodels": {
            "canonical": "Statsmodels",
            "aliases": ["statsmodels"],
            "category": "statistical_modeling",
            "domain_relevance": ["data_science", "statistics"]
        }
    },
    
    "cloud_devops": {
        "aws": {
            "canonical": "AWS",
            "aliases": ["aws", "amazon web services"],
            "category": "cloud_platform",
            "domain_relevance": ["cloud", "devops", "backend"]
        },
        "azure": {
            "canonical": "Azure",
            "aliases": ["azure", "microsoft azure"],
            "category": "cloud_platform",
            "domain_relevance": ["cloud", "devops", "backend"]
        },
        "gcp": {
            "canonical": "Google Cloud Platform",
            "aliases": ["gcp", "google cloud", "google cloud platform"],
            "category": "cloud_platform",
            "domain_relevance": ["cloud", "devops", "backend"]
        },
        "docker": {
            "canonical": "Docker",
            "aliases": ["docker", "containerization"],
            "category": "containerization",
            "domain_relevance": ["devops", "backend", "cloud"]
        },
        "kubernetes": {
            "canonical": "Kubernetes",
            "aliases": ["kubernetes", "k8s"],
            "category": "orchestration",
            "domain_relevance": ["devops", "cloud", "backend"]
        },
        "jenkins": {
            "canonical": "Jenkins",
            "aliases": ["jenkins"],
            "category": "ci_cd",
            "domain_relevance": ["devops", "automation"]
        },
        "gitlab_ci": {
            "canonical": "GitLab CI",
            "aliases": ["gitlab ci", "gitlab ci/cd"],
            "category": "ci_cd",
            "domain_relevance": ["devops", "automation"]
        },
        "github_actions": {
            "canonical": "GitHub Actions",
            "aliases": ["github actions", "gh actions"],
            "category": "ci_cd",
            "domain_relevance": ["devops", "automation"]
        },
        "terraform": {
            "canonical": "Terraform",
            "aliases": ["terraform"],
            "category": "infrastructure_as_code",
            "domain_relevance": ["devops", "cloud"]
        },
        "ansible": {
            "canonical": "Ansible",
            "aliases": ["ansible"],
            "category": "configuration_management",
            "domain_relevance": ["devops", "automation"]
        },
        "circleci": {
            "canonical": "CircleCI",
            "aliases": ["circleci", "circle ci"],
            "category": "ci_cd",
            "domain_relevance": ["devops", "automation"]
        },
        "travis": {
            "canonical": "Travis CI",
            "aliases": ["travis", "travis ci"],
            "category": "ci_cd",
            "domain_relevance": ["devops", "automation"]
        }
    },
    
    "mobile": {
        "react_native": {
            "canonical": "React Native",
            "aliases": ["react native", "react-native", "rn"],
            "category": "mobile_framework",
            "domain_relevance": ["mobile", "cross_platform"]
        },
        "flutter": {
            "canonical": "Flutter",
            "aliases": ["flutter"],
            "category": "mobile_framework",
            "domain_relevance": ["mobile", "cross_platform"]
        },
        "android_studio": {
            "canonical": "Android Studio",
            "aliases": ["android studio", "android development"],
            "category": "mobile_ide",
            "domain_relevance": ["android", "mobile"]
        },
        "xcode": {
            "canonical": "Xcode",
            "aliases": ["xcode"],
            "category": "mobile_ide",
            "domain_relevance": ["ios", "mobile"]
        },
        "jetpack_compose": {
            "canonical": "Jetpack Compose",
            "aliases": ["jetpack compose", "compose"],
            "category": "mobile_framework",
            "domain_relevance": ["android", "mobile"]
        },
        "swiftui": {
            "canonical": "SwiftUI",
            "aliases": ["swiftui", "swift ui"],
            "category": "mobile_framework",
            "domain_relevance": ["ios", "mobile"]
        },
        "ionic": {
            "canonical": "Ionic",
            "aliases": ["ionic"],
            "category": "mobile_framework",
            "domain_relevance": ["mobile", "cross_platform"]
        },
        "xamarin": {
            "canonical": "Xamarin",
            "aliases": ["xamarin"],
            "category": "mobile_framework",
            "domain_relevance": ["mobile", "cross_platform"]
        }
    },
    
    "tools": {
        "git": {
            "canonical": "Git",
            "aliases": ["git", "version control"],
            "category": "version_control",
            "domain_relevance": ["all"]
        },
        "github": {
            "canonical": "GitHub",
            "aliases": ["github"],
            "category": "platform",
            "domain_relevance": ["all"]
        },
        "gitlab": {
            "canonical": "GitLab",
            "aliases": ["gitlab"],
            "category": "platform",
            "domain_relevance": ["all"]
        },
        "vscode": {
            "canonical": "VS Code",
            "aliases": ["vscode", "vs code", "visual studio code"],
            "category": "ide",
            "domain_relevance": ["all"]
        },
        "intellij": {
            "canonical": "IntelliJ IDEA",
            "aliases": ["intellij", "intellij idea", "idea"],
            "category": "ide",
            "domain_relevance": ["java_dev", "backend"]
        },
        "postman": {
            "canonical": "Postman",
            "aliases": ["postman"],
            "category": "api_testing",
            "domain_relevance": ["backend", "api_dev"]
        },
        "jira": {
            "canonical": "Jira",
            "aliases": ["jira"],
            "category": "project_management",
            "domain_relevance": ["all"]
        },
        "pycharm": {
            "canonical": "PyCharm",
            "aliases": ["pycharm"],
            "category": "ide",
            "domain_relevance": ["python", "data_science"]
        },
        "eclipse": {
            "canonical": "Eclipse",
            "aliases": ["eclipse"],
            "category": "ide",
            "domain_relevance": ["java_dev"]
        },
        "vim": {
            "canonical": "Vim",
            "aliases": ["vim", "vi"],
            "category": "text_editor",
            "domain_relevance": ["all"]
        },
        "sublime": {
            "canonical": "Sublime Text",
            "aliases": ["sublime", "sublime text"],
            "category": "text_editor",
            "domain_relevance": ["all"]
        }
    },
    
    "big_data": {
        "hadoop": {
            "canonical": "Hadoop",
            "aliases": ["hadoop", "apache hadoop"],
            "category": "big_data_framework",
            "domain_relevance": ["big_data", "data_engineering"]
        },
        "spark": {
            "canonical": "Apache Spark",
            "aliases": ["spark", "apache spark", "pyspark"],
            "category": "big_data_framework",
            "domain_relevance": ["big_data", "data_engineering", "data_science"]
        },
        "kafka": {
            "canonical": "Apache Kafka",
            "aliases": ["kafka", "apache kafka"],
            "category": "streaming",
            "domain_relevance": ["big_data", "data_engineering", "backend"]
        },
        "airflow": {
            "canonical": "Apache Airflow",
            "aliases": ["airflow", "apache airflow"],
            "category": "workflow_orchestration",
            "domain_relevance": ["data_engineering", "ml_ops"]
        },
        "snowflake": {
            "canonical": "Snowflake",
            "aliases": ["snowflake"],
            "category": "data_warehouse",
            "domain_relevance": ["data_engineering", "analytics"]
        },
        "databricks": {
            "canonical": "Databricks",
            "aliases": ["databricks"],
            "category": "data_platform",
            "domain_relevance": ["data_engineering", "ml_ai", "big_data"]
        },
        "hive": {
            "canonical": "Apache Hive",
            "aliases": ["hive", "apache hive"],
            "category": "data_warehouse",
            "domain_relevance": ["big_data", "data_engineering"]
        },
        "flink": {
            "canonical": "Apache Flink",
            "aliases": ["flink", "apache flink"],
            "category": "streaming",
            "domain_relevance": ["big_data", "data_engineering"]
        }
    },
    
    "blockchain": {
        "solidity": {
            "canonical": "Solidity",
            "aliases": ["solidity"],
            "category": "smart_contract_language",
            "domain_relevance": ["blockchain", "web3"]
        },
        "ethereum": {
            "canonical": "Ethereum",
            "aliases": ["ethereum", "eth"],
            "category": "blockchain_platform",
            "domain_relevance": ["blockchain", "web3"]
        },
        "web3js": {
            "canonical": "Web3.js",
            "aliases": ["web3", "web3.js", "web3js"],
            "category": "blockchain_library",
            "domain_relevance": ["blockchain", "web3"]
        },
        "hardhat": {
            "canonical": "Hardhat",
            "aliases": ["hardhat"],
            "category": "blockchain_framework",
            "domain_relevance": ["blockchain", "web3"]
        },
        "truffle": {
            "canonical": "Truffle",
            "aliases": ["truffle"],
            "category": "blockchain_framework",
            "domain_relevance": ["blockchain", "web3"]
        }
    },
    
    "testing": {
        "jest": {
            "canonical": "Jest",
            "aliases": ["jest"],
            "category": "testing_framework",
            "domain_relevance": ["frontend", "backend", "testing"]
        },
        "pytest": {
            "canonical": "Pytest",
            "aliases": ["pytest", "py.test"],
            "category": "testing_framework",
            "domain_relevance": ["python", "testing"]
        },
        "junit": {
            "canonical": "JUnit",
            "aliases": ["junit"],
            "category": "testing_framework",
            "domain_relevance": ["java_dev", "testing"]
        },
        "selenium": {
            "canonical": "Selenium",
            "aliases": ["selenium"],
            "category": "testing_automation",
            "domain_relevance": ["testing", "qa"]
        },
        "cypress": {
            "canonical": "Cypress",
            "aliases": ["cypress"],
            "category": "testing_framework",
            "domain_relevance": ["frontend", "testing"]
        },
        "mocha": {
            "canonical": "Mocha",
            "aliases": ["mocha"],
            "category": "testing_framework",
            "domain_relevance": ["javascript", "testing"]
        },
        "chai": {
            "canonical": "Chai",
            "aliases": ["chai"],
            "category": "assertion_library",
            "domain_relevance": ["javascript", "testing"]
        }
    },
    
    "fintech": {
        "quantlib": {
            "canonical": "QuantLib",
            "aliases": ["quantlib"],
            "category": "financial_library",
            "domain_relevance": ["fintech", "quant"]
        },
        "yfinance": {
            "canonical": "yfinance",
            "aliases": ["yfinance", "yahoo finance"],
            "category": "financial_data",
            "domain_relevance": ["fintech", "data_science"]
        },
        "ccxt": {
            "canonical": "CCXT",
            "aliases": ["ccxt"],
            "category": "crypto_trading",
            "domain_relevance": ["fintech", "crypto", "trading"]
        },
        "alpaca": {
            "canonical": "Alpaca",
            "aliases": ["alpaca", "alpaca api"],
            "category": "trading_platform",
            "domain_relevance": ["fintech", "trading"]
        },
        "backtrader": {
            "canonical": "Backtrader",
            "aliases": ["backtrader"],
            "category": "backtesting",
            "domain_relevance": ["fintech", "trading"]
        },
        "zipline": {
            "canonical": "Zipline",
            "aliases": ["zipline"],
            "category": "backtesting",
            "domain_relevance": ["fintech", "trading"]
        },
        "ta-lib": {
            "canonical": "TA-Lib",
            "aliases": ["ta-lib", "talib", "technical analysis library"],
            "category": "technical_analysis",
            "domain_relevance": ["fintech", "trading"]
        }
    },
    
    "concepts": {
        "dsa": {
            "canonical": "Data Structures & Algorithms",
            "aliases": ["dsa", "data structures", "algorithms", "data structures and algorithms", "ds algo", "data structures & algorithms"],
            "category": "fundamental_concept",
            "domain_relevance": ["all"]
        },
        "oop": {
            "canonical": "Object-Oriented Programming",
            "aliases": ["oop", "object oriented programming", "object-oriented", "object oriented"],
            "category": "fundamental_concept",
            "domain_relevance": ["all"]
        },
        "dbms": {
            "canonical": "Database Management Systems",
            "aliases": ["dbms", "database management", "database management systems"],
            "category": "fundamental_concept",
            "domain_relevance": ["backend", "data_engineering"]
        },
        "os": {
            "canonical": "Operating Systems",
            "aliases": ["operating systems", "operating system"],
            "category": "fundamental_concept",
            "domain_relevance": ["systems", "backend"]
        },
        "networks": {
            "canonical": "Computer Networks",
            "aliases": ["computer networks", "networking", "cn"],
            "category": "fundamental_concept",
            "domain_relevance": ["backend", "systems", "devops"]
        },
        "rest_api": {
            "canonical": "REST API",
            "aliases": ["rest", "rest api", "restful", "restful api"],
            "category": "concept",
            "domain_relevance": ["backend", "fullstack"]
        },
        "graphql": {
            "canonical": "GraphQL",
            "aliases": ["graphql", "graph ql"],
            "category": "concept",
            "domain_relevance": ["backend", "fullstack"]
        },
        "microservices": {
            "canonical": "Microservices",
            "aliases": ["microservices", "microservice architecture"],
            "category": "architecture",
            "domain_relevance": ["backend", "systems", "cloud"]
        },
        "agile": {
            "canonical": "Agile",
            "aliases": ["agile", "scrum", "agile methodology"],
            "category": "methodology",
            "domain_relevance": ["all"]
        },
        "machine_learning": {
            "canonical": "Machine Learning",
            "aliases": ["machine learning", "ml", "fundamentals of ml"],
            "category": "concept",
            "domain_relevance": ["ml_ai", "data_science"]
        },
        "deep_learning": {
            "canonical": "Deep Learning",
            "aliases": ["deep learning", "dl", "neural networks"],
            "category": "concept",
            "domain_relevance": ["ml_ai", "ai"]
        },
        "nlp": {
            "canonical": "Natural Language Processing",
            "aliases": ["nlp", "natural language processing"],
            "category": "concept",
            "domain_relevance": ["ml_ai", "ai"]
        },
        "computer_vision": {
            "canonical": "Computer Vision",
            "aliases": ["computer vision", "cv"],
            "category": "concept",
            "domain_relevance": ["ml_ai", "ai"]
        },
        "linux": {
            "canonical": "Linux",
            "aliases": ["linux", "unix"],
            "category": "operating_system",
            "domain_relevance": ["devops", "backend", "systems"]
        }
    },
    
    "trading_concepts": {
        "technical_analysis": {
            "canonical": "Technical Analysis",
            "aliases": ["technical analysis", "ta", "chart analysis"],
            "category": "trading_concept",
            "domain_relevance": ["fintech", "trading"]
        },
        "algorithmic_trading": {
            "canonical": "Algorithmic Trading",
            "aliases": ["algorithmic trading", "algo trading", "automated trading"],
            "category": "trading_concept",
            "domain_relevance": ["fintech", "trading"]
        },
        "portfolio_optimization": {
            "canonical": "Portfolio Optimization",
            "aliases": ["portfolio optimization", "portfolio management"],
            "category": "trading_concept",
            "domain_relevance": ["fintech", "quant"]
        },
        "risk_management": {
            "canonical": "Risk Management",
            "aliases": ["risk management", "risk analysis"],
            "category": "trading_concept",
            "domain_relevance": ["fintech", "quant"]
        },
        "monte_carlo": {
            "canonical": "Monte Carlo Simulation",
            "aliases": ["monte carlo", "monte carlo simulation", "monte carlo simulations"],
            "category": "quantitative_method",
            "domain_relevance": ["fintech", "quant", "data_science"]
        }
    },
    "cybersecurity": {
    "wireshark": {
        "canonical": "Wireshark",
        "aliases": ["wireshark"],
        "category": "network_analysis",
        "domain_relevance": ["cybersecurity", "networks"]
    },
    "metasploit": {
        "canonical": "Metasploit",
        "aliases": ["metasploit"],
        "category": "penetration_testing",
        "domain_relevance": ["cybersecurity"]
    },
    "burpsuite": {
        "canonical": "Burp Suite",
        "aliases": ["burp", "burp suite"],
        "category": "security_testing",
        "domain_relevance": ["cybersecurity"]
    },
    "nmap": {
        "canonical": "Nmap",
        "aliases": ["nmap"],
        "category": "network_scanning",
        "domain_relevance": ["cybersecurity"]
    },
    "kali_linux": {
        "canonical": "Kali Linux",
        "aliases": ["kali linux", "kali"],
        "category": "security_os",
        "domain_relevance": ["cybersecurity"]
    }
    },
    "ai_llm": {
    "langchain": {
        "canonical": "LangChain",
        "aliases": ["langchain"],
        "category": "llm_framework",
        "domain_relevance": ["ml_ai", "llm"]
    },
    "openai_api": {
        "canonical": "OpenAI API",
        "aliases": ["openai api", "gpt api"],
        "category": "llm_platform",
        "domain_relevance": ["ml_ai", "llm"]
    },
    "llama": {
        "canonical": "LLaMA",
        "aliases": ["llama", "llama2"],
        "category": "llm_model",
        "domain_relevance": ["ml_ai", "llm"]
    },
    "prompt_engineering": {
        "canonical": "Prompt Engineering",
        "aliases": ["prompt engineering"],
        "category": "llm_skill",
        "domain_relevance": ["ml_ai", "llm"]
    }
},
    "data_engineering_tools": {
    "dbt": {
        "canonical": "dbt",
        "aliases": ["dbt"],
        "category": "data_transformation",
        "domain_relevance": ["data_engineering"]
    },
    "kinesis": {
        "canonical": "Amazon Kinesis",
        "aliases": ["kinesis"],
        "category": "streaming",
        "domain_relevance": ["data_engineering", "cloud"]
    },
    "bigquery": {
        "canonical": "BigQuery",
        "aliases": ["bigquery", "google bigquery"],
        "category": "data_warehouse",
        "domain_relevance": ["data_engineering", "analytics"]
    }
},
    "game_dev": {
    "unity": {
        "canonical": "Unity",
        "aliases": ["unity"],
        "category": "game_engine",
        "domain_relevance": ["game_dev"]
    },
    "unreal": {
        "canonical": "Unreal Engine",
        "aliases": ["unreal", "unreal engine"],
        "category": "game_engine",
        "domain_relevance": ["game_dev"]
    }
},
    "embedded_iot": {
    "arduino": {
        "canonical": "Arduino",
        "aliases": ["arduino"],
        "category": "embedded_platform",
        "domain_relevance": ["embedded", "iot"]
    },
    "raspberry_pi": {
        "canonical": "Raspberry Pi",
        "aliases": ["raspberry pi"],
        "category": "embedded_platform",
        "domain_relevance": ["embedded", "iot"]
    }
},
    "analytics_tools": {
    "powerbi": {
        "canonical": "Power BI",
        "aliases": ["powerbi", "power bi"],
        "category": "bi_tool",
        "domain_relevance": ["analytics", "data_science"]
    },
    "tableau": {
        "canonical": "Tableau",
        "aliases": ["tableau"],
        "category": "bi_tool",
        "domain_relevance": ["analytics", "data_science"]
    }
}


}


sections_map = {
    "summary": [
        "summary", "professional summary", "career summary", "executive summary", "profile", 
        "professional profile", "personal profile", "objective", "career objective", 
        "professional objective", "summary of qualifications", "qualifications summary", 
        "highlights", "professional highlights", "key qualifications", "overview", 
        "career overview", "introduction", "about me"
    ],
    "projects": [
        "projects", "relevant projects", "key projects", "selected projects", "project experience", 
        "portfolio", "personal projects", "academic projects", "professional projects", "projects and initiatives",
        "major projects", "project highlights", "case studies", "work samples", "initiatives",
        "development projects", "research projects", "engineering projects", "design projects", "projects & initiatives",
        "software projects"
    ],
    "experience": [
        "experience", "work experience", "professional experience", "employment history", 
        "career history", "relevant experience", "job history", "work history", 
        "professional history", "career experience", "employment experience", 
        "internship experience", "volunteer experience", "leadership experience", 
        "teaching experience", "research experience"
    ],
    "skills": [
        "skills", "technical skills", "technologies", "core competencies", "tools", 
        "key skills", "professional skills", "areas of expertise", "competencies", 
        "proficiencies", "abilities", "strengths", "technical proficiencies", 
        "software skills", "programming skills", "language skills", "soft skills", 
        "hard skills", "expertise", "specializations", "capabilities", "qualifications"
    ],
    "education": [
        "education", "academic background", "educational qualifications", "degrees", 
        "certifications", "training", "academic history", "qualifications", 
        "education and training", "academic credentials", "professional development", 
        "courses", "diplomas", "degrees and certifications", "educational background", 
        "schooling", "formal education", "higher education"
    ]
}



#confidence detect
SIGNAL_MAP = {
    "weak": {
        "basics", "fundamentals", "intro", "learning", "studied", "familiar"
    },

    "medium": {
        "used", "implemented", "worked", "applied",
        "built", "developed", "created", "handled",
        "configured", "integrated"
    },

    "strong": {
        "designed", "deployed", "optimized", "led",
        "architected", "automated", "managed",
        "engineered", "reduced", "improved",
        "scaled", "orchestrated"
    }
}