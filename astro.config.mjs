// @ts-check
import { defineConfig } from "astro/config"
import starlight from "@astrojs/starlight"
import starlightLinksValidator from "starlight-links-validator"

export default defineConfig({
  site: "https://muhlenberg-cs.github.io",
  integrations: [
    starlight({
      title: "CSI 370 · CUE",
      description: "Capstone software engineering with MuleCode, Muhlenberg College, Spring 2027",
      logo: { src: "./src/assets/mulecode-app-icon.svg", alt: "" },
      favicon: "/favicon.svg",
      customCss: ["@fontsource/jetbrains-mono/400.css", "@fontsource/jetbrains-mono/700.css", "./src/styles/brand.css"],
      social: [{ icon: "github", label: "muhlenberg-cs on GitHub", href: "https://github.com/muhlenberg-cs" }],
      lastUpdated: true,
      plugins: [starlightLinksValidator()],
      sidebar: [
        {
          label: "Start here",
          items: [
            { label: "Before the first class", slug: "start" },
            { label: "1. GitHub and Classroom", slug: "start/github" },
            { label: "2. Install mule", slug: "start/install-mule" },
            { label: "3. Ollama and the model", slug: "start/ollama" },
            { label: "4. Terminal and font", slug: "start/terminal" },
            { label: "5. Sign in to gh", slug: "start/gh" },
            { label: "6. Check it all works", slug: "start/check" },
          ],
        },
        { label: "Schedule", slug: "schedule" },
        {
          label: "MuleCode guide",
          items: [
            { label: "Modes and stages", slug: "mule/modes" },
            { label: "Commands", slug: "mule/commands" },
            { label: "Icebergs", slug: "mule/iceberg" },
            { label: "When mule says no", slug: "mule/sandbox" },
            { label: "Troubleshooting", slug: "mule/troubleshooting" },
          ],
        },
        {
          label: "GitHub guide",
          items: [
            { label: "Git in one page", slug: "github/git" },
            { label: "The team flow", slug: "github/team-flow" },
            { label: "Reading CI", slug: "github/ci" },
            { label: "Sprints and the board", slug: "github/sprints" },
          ],
        },
        { label: "Assignments", slug: "assignments" },
        { label: "Policies", slug: "policies" },
        { label: "Videos", slug: "videos" },
      ],
    }),
  ],
})
