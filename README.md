# 🛍️ Google Immersive Product API: rich product pages as clean JSON

> The most efficient, reliable, and developer-friendly way to use the Google Immersive Product API.

**Actor page:** [apify.com/johnvc/google-immersive-product-api](https://apify.com/johnvc/google-immersive-product-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-immersive-product-api/input-schema](https://apify.com/johnvc/google-immersive-product-api/input-schema?fpr=9n7kx3)

Get Google's rich immersive product pages for any product search as structured JSON. Give the API a product query and get the deep product detail page Google shows shoppers, for the top matching products: title, brand, price range across stores, the aggregated rating and star-by-star review breakdown, specs, variants, the stores selling it, related videos, and sample user reviews.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Immersive-Product-API.git
   cd Apify-Google-Immersive-Product-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run an example**
   ```bash
   # Single example:
   uv run python google-immersive-product-api-example.py

   # Batch example (searches several product categories in one run):
   uv run python google-immersive-product-api-batch-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-immersive-product-api-example.py
```

## Why Use This Google Immersive Product API?

The full product page, structured. Specs, ratings, variants, stores, and reviews in one row per product.

Clean, predictable JSON. Load it straight into a dataframe, a database, or an AI shopping agent.

Built for product research. Compare ratings, prices, and specs across competing products in one run.

MCP-ready. AI agents can call it as a tool through the hosted Apify MCP server.

## Features

### Core Capabilities
- Rich product detail pages for the top products matching a query
- Aggregated rating plus a star-by-star review breakdown
- Specs, variants, stores, videos, and sample user reviews
- Batch several product queries in one run

### Data Quality
- One clean row per product, tagged with the source query
- Stable JSON shape, easy to load anywhere

## Usage Examples

### Basic Example
```json
{
  "query": "running shoes"
}
```

### Advanced Example
```json
{
  "queries": ["running shoes", "wireless earbuds"],
  "gl": "us",
  "maxResultsPerQuery": 10
}
```

For a runnable batch script, see `google-immersive-product-api-batch-example.py` in this repo.

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | one of | - | A single product search, e.g. `running shoes`. |
| `queries` | `list[str]` | one of | - | A batch of product searches. Merged with `query` and de-duplicated. |
| `gl` | `str` | no | `"us"` | Two-letter country code for pricing and localization. |
| `hl` | `str` | no | `"en"` | Two-letter language code. |
| `maxResultsPerQuery` | `int` | no | `10` | Products per query to pull the rich page for (maximum 20). |

## Output Format

Each item in the dataset is one product:

```json
{
  "result_type": "product",
  "query": "running shoes",
  "position": 1,
  "title": "Adidas Men's Adizero Evo SL",
  "brand": "adidas",
  "price_range": "$150-$150",
  "rating": 4.8,
  "reviews": 19093,
  "ratings": [ { "stars": 5, "amount": 16553 } ],
  "thumbnails": [ "https://..." ]
}
```

---

<!-- The five install sections below are the canonical MCP install copy. -->
## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Immersive Product API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-immersive-product-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Immersive Product API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-immersive-product-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-immersive-product-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Immersive Product API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-immersive-product-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-immersive-product-api`, using OAuth when prompted.
5. Ask Claude to run the Google Immersive Product API.

Open Claude on the web: https://claude.ai

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-immersive-product-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-immersive-product-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Immersive Product API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/google-immersive-product-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Immersive Product API to power product research in your e-commerce tools or AI agent.*

## Featured Tasks

Ready-to-run examples on the Apify Store, each targeting one product research use case:

- [Get Rich Product Detail Pages From a Google Search](https://apify.com/johnvc/google-immersive-product-api/examples/get-rich-product-detail-pages-from-a-google-search?fpr=9n7kx3)
- [Get a Product's Ratings and Reviews From Google](https://apify.com/johnvc/google-immersive-product-api/examples/get-a-product-s-ratings-and-reviews-from-google?fpr=9n7kx3)
- [Get Apple Watch Prices and Ratings as JSON](https://apify.com/johnvc/google-immersive-product-api/examples/get-apple-watch-prices-and-ratings-as-json?fpr=9n7kx3)
- [Get Laptop Prices, Brands, and Ratings as JSON](https://apify.com/johnvc/google-immersive-product-api/examples/get-laptop-prices-brands-and-ratings-as-json?fpr=9n7kx3)

Last Updated: 2026.07.05
