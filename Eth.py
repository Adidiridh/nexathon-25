sequenceDiagram
    actor User
    participant SEO_Agent as SEO Agent
    participant Scraper_Agent as Website Scraper Agent

    activate User
    User->>SEO_Agent: Send SEORequest (URL)
    activate SEO_Agent
    SEO_Agent->>Scraper_Agent: WebsiteScraperRequest (URL)
    activate Scraper_Agent
    Scraper_Agent->>SEO_Agent: WebsiteScraperResponse (Content)
    deactivate Scraper_Agent

    SEO_Agent->>SEO_Agent: Extract Keywords from Content
    SEO_Agent->>SEO_Agent: Perform SERP Lookup (Extract top URLs)

    SEO_Agent->>Scraper_Agent: WebsiteScraperRequest (Top URL)
    activate Scraper_Agent
    Scraper_Agent->>SEO_Agent: WebsiteScraperResponse (Top Content)
    deactivate Scraper_Agent

    SEO_Agent->>SEO_Agent: Compare Content (SEO analysis)
    SEO_Agent->>User: SEOResponse (Comparison Results)
    deactivate SEO_Agent

