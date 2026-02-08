# AI Agent Skills Collection

This repository is a curated collection of skills I've developed for AI agents, aimed at automating and enhancing productivity in software development and related tasks. These skills follow the [Agent Skills](https://agentskills.io) format, making them easy to integrate into AI systems for streamlined workflows.

Currently, the repository features the **DocFactory suite**, a comprehensive set of skills for generating professional documentation for mobile app projects. Future updates will include additional skills for other domains.

## Purpose

AI agents are powerful tools, but their effectiveness depends on well-defined skills that guide their actions. This collection provides ready-to-use skills that you can incorporate into your own AI setups, whether for personal projects, team collaboration, or open-source contributions. By sharing these skills, I hope to foster innovation and efficiency in AI-assisted development.

## Features

- **Modular Design**: Each skill is self-contained, targeting specific tasks for easy adoption and customization.
- **Standardized Format**: All skills adhere to the Agent Skills framework for compatibility.
- **Comprehensive Documentation**: Includes templates, references, examples, and validation scripts.
- **Open for Expansion**: Designed to grow with new skills as I develop them.
- **Quality Assurance**: Built-in validators ensure outputs meet high standards.

## Skills Overview

The repository currently includes the following skills from the DocFactory suite, which automate documentation for mobile app development:

1. **[docfactory-init](skills/docfactory-init/)**: Generates foundational documents (`00-project-brief.md`, `00-decisions.md`, `00-glossary.md`) from an initial idea capsule.
2. **[docfactory-market](skills/docfactory-market/)**: Conducts market research and competitor analysis (`01-market-research.md`).
3. **[docfactory-prd](skills/docfactory-prd/)**: Creates a Product Requirements Document (`02-prd.md`) with user stories and monetization strategies.
4. **[docfactory-uiux](skills/docfactory-uiux/)**: Develops UI/UX specifications (`03-ui-ux-spec.md`) including screen specs and accessibility checklists.
5. **[docfactory-arch](skills/docfactory-arch/)**: Drafts technical architecture documentation (`04-tech-architecture.md`) covering stack, data layer, and deployment.
6. **[docfactory-backlog](skills/docfactory-backlog/)**: Generates a prioritized backlog (`06-backlog.md`) with task cards and estimation rubrics.
7. **[docfactory-audit](skills/docfactory-audit/)**: Performs consistency audits (`09-consistency-audit.md`) to ensure project coherence.

These skills are designed to be used in sequence for optimal results in mobile app documentation.

## Installation

To use any skill in this repository:

1. Clone this repository:

   ```bash
   git clone https://github.com/burakdirin/skills.git
   cd skills
   ```

2. Copy the desired skill directory from the `skills/` folder into your agent's configured skills directory.

For skills requiring local validation or generation (e.g., those with Python scripts), ensure Python 3.x is installed along with any specified dependencies (e.g., PyYAML).

## Usage

1. Review the skill's `README.md` and `SKILL.md` for prerequisites, inputs, and outputs.
2. Integrate the skill into your AI agent as per the Agent Skills framework.
3. Run validation scripts if available to verify outputs.
4. Customize templates and references to fit your needs.

For the DocFactory suite, start with `docfactory-init` and proceed sequentially.

## Examples

Each skill includes example inputs and outputs in its `examples/` folder. Refer to these for practical usage.

## Contributing

Contributions are welcome! Whether it's improving existing skills, adding new ones, or enhancing documentation:

1. Fork the repository.
2. Create a feature branch.
3. Ensure validations pass.
4. Submit a pull request.

For new skill ideas, open an issue to discuss.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions or issues, please open a GitHub issue or contact the maintainer.

---

_Empowering AI agents, one skill at a time._
