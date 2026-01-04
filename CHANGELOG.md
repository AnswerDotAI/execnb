# Release notes

<!-- do not remove -->

## 0.1.18

### Bugs Squashed

- id not extracted from cell meta ([#80](https://github.com/AnswerDotAI/execnb/issues/80))


## 0.1.17

### New Features

- Add cell id in nbio ([#79](https://github.com/AnswerDotAI/execnb/issues/79))


## 0.1.16

### Bugs Squashed

- Catch errors before exec ([#77](https://github.com/AnswerDotAI/execnb/issues/77))


## 0.1.15

### New Features

- Add --verbose flag to `exec_nb` for real-time output ([#75](https://github.com/AnswerDotAI/execnb/pull/75)), thanks to [@radekosmulski](https://github.com/radekosmulski)


## 0.1.14

### New Features

- Support for graphviz and other svg rendering in outputs ([#73](https://github.com/AnswerDotAI/execnb/pull/73)), thanks to [@curtis-allan](https://github.com/curtis-allan)


## 0.1.12

### New Features

- Allow render outputs to take in functions that can modify HTML prior to being returned ([#72](https://github.com/AnswerDotAI/execnb/pull/72)), thanks to [@Isaac-Flath](https://github.com/Isaac-Flath)
- Use fastcore `strip_ansi` instead of ipython text ([#71](https://github.com/AnswerDotAI/execnb/pull/71)), thanks to [@erikgaas](https://github.com/erikgaas)


## 0.1.11

### New Features

- Limit to param names in completions if available ([#67](https://github.com/AnswerDotAI/execnb/issues/67))


## 0.1.10

### Bugs Squashed

- `execution_count` and traceback formatted incorrectly ([#66](https://github.com/AnswerDotAI/execnb/issues/66))


## 0.1.9

### New Features

- add `shell.run_async` ([#63](https://github.com/AnswerDotAI/execnb/pull/63)), thanks to [@comhar](https://github.com/comhar)
- Use pygments for md output rendering ([#62](https://github.com/AnswerDotAI/execnb/issues/62))
- Add optional image rendering control to `render_outputs` ([#61](https://github.com/AnswerDotAI/execnb/pull/61)), thanks to [@ncoop57](https://github.com/ncoop57)
- Add option to use ansi2html renderer ([#57](https://github.com/AnswerDotAI/execnb/pull/57)), thanks to [@Isaac-Flath](https://github.com/Isaac-Flath)

### Bugs Squashed

- Missing execution count in run cells ([#65](https://github.com/AnswerDotAI/execnb/issues/65))
- Fix matplotlib rendering in `render_outputs` ([#64](https://github.com/AnswerDotAI/execnb/pull/64)), thanks to [@johnowhitaker](https://github.com/johnowhitaker)


## 0.1.8

### New Features

- Add support for timeouts in CaptureShell ([#60](https://github.com/fastai/execnb/issues/60))
- Add `render_outputs` ([#55](https://github.com/fastai/execnb/issues/55))
- Add SmartCompleter ([#54](https://github.com/fastai/execnb/issues/54))
- Major refactor of CaptureShell ([#53](https://github.com/fastai/execnb/issues/53))
- add markdown to doc output ([#52](https://github.com/fastai/execnb/issues/52))

### Bugs Squashed

- Use `callable` instead of `Callable` ([#59](https://github.com/fastai/execnb/issues/59))


## 0.1.6

- New functions for extracting outputs


## 0.1.5

### New Features

- Add `DummyHistory` ([#38](https://github.com/fastai/execnb/issues/38))

### Bugs Squashed

- `CaptureShell.enable_matplotlib` does not follow its parent's interface ([#42](https://github.com/fastai/execnb/issues/42))
- Specify encoding when reading file in `write_nb` ([#41](https://github.com/fastai/execnb/pull/41)), thanks to [@RalfG](https://github.com/RalfG)


## 0.1.4


### Bugs Squashed

- `CaptureShell.shell` sets `cell.outputs` to ordinary dicts instead of `AttrDict`s ([#39](https://github.com/fastai/execnb/pull/39)), thanks to [@seeM](https://github.com/seeM)


## 0.1.3

### New Features

- Add `DummyHistory` ([#38](https://github.com/fastai/execnb/issues/38))

### Bugs Squashed

- `nbdev_test` fails due to unescaped backslash in windows path ([#37](https://github.com/fastai/execnb/issues/37))


## 0.1.2

### New Features

- Only write file if changed in `write_nb` ([#35](https://github.com/fastai/execnb/issues/35))
- faster startup with `MPLBACKEND` environment variable to lazily set matplotlib backend ([#33](https://github.com/fastai/execnb/pull/33)), thanks to [@seeM](https://github.com/seeM)


## 0.1.1

### New Features

- Support `ipywidgets` ([#24](https://github.com/fastai/execnb/issues/24))

### Bugs Squashed

- Seaborn is not compatible with execnb ([#27](https://github.com/fastai/execnb/issues/27))


## 0.1.0

### New Features

- Remove usage of fastcore.xtras and fastcore.foundation to reduce chance of macOS fork issue ([#26](https://github.com/fastai/execnb/issues/26))


## 0.0.10

### New Features

- add `mk_cell` ([#25](https://github.com/fastai/execnb/issues/25))
- Add new nb function ([#23](https://github.com/fastai/execnb/pull/23)), thanks to [@dleen](https://github.com/dleen)
- Parameterize Notebooks ([#19](https://github.com/fastai/execnb/issues/19))
  - (This was completed earlier but not marked done in gh issues)


## 0.0.9

### New Features

- use fork mode on mac ([#22](https://github.com/fastai/execnb/issues/22))


## 0.0.8

- Use nbdev2


## 0.0.6

### Bugs Squashed

- do not fail if matplotlib is not installed when running  `%matplotlib inline` ([#6](https://github.com/fastai/execnb/pull/6)), thanks to [@hamelsmu](https://github.com/hamelsmu)


## 0.0.3

- Add notebook dir to python path


## 0.0.2

- Compat with nbdev test runner


## 0.0.1

- Initial release

