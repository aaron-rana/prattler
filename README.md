# prattler

**prattler** is a lightweight custom sensor for [Home Assistant](https://www.home-assistant.io/) that generates context-aware greeting messages based on time, weather, and mood. It reads from a customizable `greeting.yaml` file, allowing you to personalize how Home Assistant greets you.

---

## Features

- Dynamic greetings based on time of day, weather, and more
- Fully customizable via YAML
- Simple setup, zero dependencies

---

## Installation (via HACS)

1. In Home Assistant, go to **HACS > Integrations**.
2. Click the **⋮ (three-dot menu)** > **Custom Repositories**.
3. Add this repository URL:
https://github.com/aaron-rana/prattler

Set category to **Integration**, then click **Add**.

4. Find **prattler** in the list of integrations and click **Install**.
5. **Restart Home Assistant** once installation is complete.

---

## Configuration

Add the following to your `configuration.yaml`:

```yaml
# prattler
sensor:
- platform: prattler
