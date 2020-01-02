# configuration

See documentation [here](doc/00-overview.md)

``` yaml
use-extension:
  "@autorest/cli.common": "latest"
  "@autorest/fakesdk": "latest"
  "az": "$(this-folder)"

pipeline-model: v3
clicommon: true
fakesdk123: true
pipeline:
    az:
        input: fakesdk
        output-artifact: source-file-fakesdk-inaz
    az/aznamer:
        plugin: fakenamer
        input: cli.common
        output-artifact: source-file-cli
    az/renamer:
        input: az/aznamer
        output-artifact: source-file-cli
    az/emitter:
        input:
            - az
            - az/renamer
        scope: scope-here

scope-here:
    is-object: false
    output-artifact:
        - source-file-cli
        - source-file-fakesdk-inaz
```
