# Changelog

## [0.6.0](https://github.com/sudoblockio/tackle/compare/v0.5.1...v0.6.0) (2024-12-21)


### Features

* add Context and HookCallInput args to all native providers ([677a482](https://github.com/sudoblockio/tackle/commit/677a4826c0f83cc0fc28bc2df566fe8b2e9f741c))
* add decorator for exposing python hooks and methods ([f772e38](https://github.com/sudoblockio/tackle/commit/f772e38f99cf5e8017536e8a02cf2ecf2cb821e1))
* add function to join kwargs into single string and implement  syntax ([6dad877](https://github.com/sudoblockio/tackle/commit/6dad877cb79aa445456638e2dd0d2ae6a646c298))
* add import hook which takes flexible arguments in both special keys, str, and list[str|dict] ([5fc3a97](https://github.com/sudoblockio/tackle/commit/5fc3a97c3cde3230d2d4266434ab25e44dfae861))
* add pipes in types for union - ie str|int = Union[str,int] ([3961c48](https://github.com/sudoblockio/tackle/commit/3961c48b5a23c9ed9b69faabbdad0cb813292503))
* allow for python hook names to be implied by class name ([d2ebf17](https://github.com/sudoblockio/tackle/commit/d2ebf172e44ff7378d8f5aca79c606da00264a1f))
* change hook_name to classvar ([a979588](https://github.com/sudoblockio/tackle/commit/a97958818cb795ff364b8e5d2af289252bb31254))
* implement functions through macro ([fe8dccf](https://github.com/sudoblockio/tackle/commit/fe8dccffb5f8cadcada574a768e316ba1afc863a))
* implement validator logic in hook field and rewrite the majority of dcl hook logic for pydantic 2 ([62aeeb6](https://github.com/sudoblockio/tackle/commit/62aeeb624371f8e6c3612260082e47ce01ac935d))
* major parser changes including data splitting (pre/hook-call/post), hook context injection, along with numerous bugs ([57d5904](https://github.com/sudoblockio/tackle/commit/57d59045e07eb2602fe0667fd8996b66f22f29df))
* make field hooks callable via a default factory ([110a1b0](https://github.com/sudoblockio/tackle/commit/110a1b0b236607cb04d960b09c7564eae23bd4af))
* rewrite tackle for v0.6 - too many features to list - see notes ([4e66f17](https://github.com/sudoblockio/tackle/commit/4e66f1768c84e23ff70257a92fbe61f0177a5e4b))
* support pydantic, datetime, and ipaddress types as field types in a hook ([f4d20fd](https://github.com/sudoblockio/tackle/commit/f4d20fd73607e81eedb7e8a2a241e14de75c7325))
* update the jinja environment to Native so that python types are returned as is ([f706817](https://github.com/sudoblockio/tackle/commit/f7068174eb39ab9b6234e08a39b44154ac1b4ac1))


### Bug Fixes

* add ability to import hooks inside python hooks ([5bfde69](https://github.com/sudoblockio/tackle/commit/5bfde6946cc9939437f87daeda6c47fff0b532c0))
* add string serializer for special field types ([2dda7de](https://github.com/sudoblockio/tackle/commit/2dda7de93ab0912d030cd3090820836d6920b6c7))
* breaking - don't write to temporary data within loop as never needed ([9acf46d](https://github.com/sudoblockio/tackle/commit/9acf46d08b42f089dbc830667601f6524b38cfdb))
* calling directory vars be preserved in child dir calls ([5e790d8](https://github.com/sudoblockio/tackle/commit/5e790d88b504bc6d721d42b9a63fc741a40fa6e2))
* create_source for args with non-str args and find_in_parent ([658bbbe](https://github.com/sudoblockio/tackle/commit/658bbbee3d229680e6d53b2e1f99adbe6cb026ed))
* empty list not being set for false conditionals ([0cf914e](https://github.com/sudoblockio/tackle/commit/0cf914eb37f01faefccc39d3ce4eebda04f6731d))
* exclude some params like args and help on dump - tmp fix while serde stuff is all messed up ([6cf2b8f](https://github.com/sudoblockio/tackle/commit/6cf2b8f7e67dc22a42b8051944c14e7532f651ff))
* failing tests from abs path now as calling_file special var ([5a5b2d0](https://github.com/sudoblockio/tackle/commit/5a5b2d0b1301551b75b23d04bfd740c17b0aa024))
* make context hooks sep a dot by default vs slash ([49c8df9](https://github.com/sudoblockio/tackle/commit/49c8df95e154dc09690202643346b1c284c4bc8e))
* update generate hook and add convert_template_filenames field ([9cf9e2d](https://github.com/sudoblockio/tackle/commit/9cf9e2d16d2616b8b29ad559c0e7d585e65191b1))
* vcs not using version when specified by rebuilding git logic [#75](https://github.com/sudoblockio/tackle/issues/75) [#76](https://github.com/sudoblockio/tackle/issues/76) ([dabd5f1](https://github.com/sudoblockio/tackle/commit/dabd5f1495a2a5f16e5774c6d5a1ad60956a2dca))


### Refactors

* context and hook_call out of BaseHook and change to dataclass instead of BaseModel [#178](https://github.com/sudoblockio/tackle/issues/178) ([52bbc55](https://github.com/sudoblockio/tackle/commit/52bbc55d486aacef11b325dcf00e5586bbc61fe6))
* hook_type to hook_name (breaking change) ([663578a](https://github.com/sudoblockio/tackle/commit/663578a44494598e6dc38f87897450082235268b))
* parser logic to work with pyd2 ([64bcd02](https://github.com/sudoblockio/tackle/commit/64bcd0277f89fa17ef4a9db5949bff8a7333a98d))


### Provider Changes

* add  hook ([6a6abd9](https://github.com/sudoblockio/tackle/commit/6a6abd96a35a917595c8f220e2fb8016855875ae))
* update block hook to new convention maintaining tests ([174a7bf](https://github.com/sudoblockio/tackle/commit/174a7bf790dc617017218255df69a03ad87df542))
* update match hook to new convention which breaks tests with merge / conditional (2 tests) ([9159fd5](https://github.com/sudoblockio/tackle/commit/9159fd56d82a925fffbd4ab37aec4900f5864363))

## [0.5.1](https://github.com/sudoblockio/tackle/compare/v0.5.0...v0.5.1) (2023-07-17)


### Bug Fixes

* issue with hook defaults being overwritten when called - remove unneeded code modifies hook ([d1dbde0](https://github.com/sudoblockio/tackle/commit/d1dbde0b2fb4cfcf163d6845bca1d1755fbc06f2))
* regression in how args are parsed in main ([c9369b2](https://github.com/sudoblockio/tackle/commit/c9369b2a92e575befd35c54ca38624d73269ddb7))

## [0.5.0](https://github.com/sudoblockio/tackle/compare/v0.4.11...v0.5.0) (2023-06-18)


### Features

* add enum as field type for declarative hooks ([5982df2](https://github.com/sudoblockio/tackle/commit/5982df29fc0c729be134903cc66d845d618b9134))
* remove need to calling hook methods with a period [#158](https://github.com/sudoblockio/tackle/issues/158) - refactor get_hook ([6da2cbe](https://github.com/sudoblockio/tackle/commit/6da2cbea525445f927c2d4a9fea501f436c5cd21))


### Bug Fixes

* add better exception handling for hook call ([877c3fb](https://github.com/sudoblockio/tackle/commit/877c3fb94e7627f5f3d24632112fdd956ccb0a1b))
* allow hook merging into dicts ([#107](https://github.com/sudoblockio/tackle/issues/107)) and fix index issue with merging into lists ([2bccc8c](https://github.com/sudoblockio/tackle/commit/2bccc8c010166c6595af65d246cce6986e3aef36))
* calling hook with kwargs field within loop [#166](https://github.com/sudoblockio/tackle/issues/166) ([db76ea8](https://github.com/sudoblockio/tackle/commit/db76ea806485aa03957b87cfcf0085ef88824b7b))
* match / block hook not handling existing contexts properly [#57](https://github.com/sudoblockio/tackle/issues/57) [#45](https://github.com/sudoblockio/tackle/issues/45) [#51](https://github.com/sudoblockio/tackle/issues/51) ([f47e211](https://github.com/sudoblockio/tackle/commit/f47e21160c40acfb779401e0306a5bf3a0796100))


### Refactors

* many functions within the parser ([62bdf21](https://github.com/sudoblockio/tackle/commit/62bdf21c9416d4ab161b448c5353de9c49c8f45d))

## [0.4.11](https://github.com/sudoblockio/tackle/compare/v0.4.10...v0.4.11) (2023-03-14)


### Bug Fixes

* add better exception handling for missing key in match hook ([64c9ee1](https://github.com/sudoblockio/tackle/commit/64c9ee1236ddee7045361108ff3734ba7ace547e))
* error context showing None for ([4b1d1fe](https://github.com/sudoblockio/tackle/commit/4b1d1fe380041249d6b24dcddfd603828f77e23a))

## [0.4.10](https://github.com/sudoblockio/tackle/compare/v0.4.9...v0.4.10) (2022-12-28)


### Provider Changes

* add more options to filter hidden files / dirs in  hook ([bb53f3d](https://github.com/sudoblockio/tackle/commit/bb53f3d90e0a672b96b02f6ea1e047814bd83f02))

## [0.4.9](https://github.com/sudoblockio/tackle/compare/v0.4.8...v0.4.9) (2022-12-20)


### Bug Fixes

* allow ambiguous keys like 'namespace' to be used as string renderables ([c1f1886](https://github.com/sudoblockio/tackle/commit/c1f18862feced7c32aaf4538b4b2737cebacfea3))

## [0.4.8](https://github.com/sudoblockio/tackle/compare/v0.4.7...v0.4.8) (2022-12-14)


### Bug Fixes

* no_input not being carried into declarative hook calls ([236aa4a](https://github.com/sudoblockio/tackle/commit/236aa4a39e378c77dac23753e7ef2ee14081b429))

## [0.4.7](https://github.com/sudoblockio/tackle/compare/v0.4.6...v0.4.7) (2022-12-12)


### Bug Fixes

* override blocks / nested inputs ([3601fd5](https://github.com/sudoblockio/tackle/commit/3601fd556d207911ccd501c1bd9a8bae48a9c35a))
* override inputs so that they are able to apply to declarative hook execs and are passed through remote calls ([d3ccf0a](https://github.com/sudoblockio/tackle/commit/d3ccf0aed8fd60d3e287a98cc166e5817f859023))

## [0.4.6](https://github.com/sudoblockio/tackle/compare/v0.4.5...v0.4.6) (2022-12-07)


### Bug Fixes

* render vars coming from  field in hook that maps a dict to fields ([df6846b](https://github.com/sudoblockio/tackle/commit/df6846b6b8aaf8e3de7b8eebc6735c90a463a1c5))

## [0.4.5](https://github.com/sudoblockio/tackle/compare/v0.4.4...v0.4.5) (2022-12-06)


### Bug Fixes

* error using method from hook from  dir [#113](https://github.com/sudoblockio/tackle/issues/113) ([1dbf214](https://github.com/sudoblockio/tackle/commit/1dbf2142b29d2c4e3bf07308556ee17e241804a5))
* render return in dcl hook ([9970987](https://github.com/sudoblockio/tackle/commit/99709873845124128fb92ec1c61e3a030f2d29bb))


### Provider Changes

* allow yaml hook to read documents as lists ([f2fa091](https://github.com/sudoblockio/tackle/commit/f2fa09168bd8784eeab14e1160a9680a7b304c80))


### Refactors

* clean up function_exceptions test ([7c73c31](https://github.com/sudoblockio/tackle/commit/7c73c312e25777bb30c3d329549d3dc44e0a80be))
* more stuff to sudoblockio ([77615b1](https://github.com/sudoblockio/tackle/commit/77615b160d77122e3520aab5d90d38e258986df1))
* move repo to sudoblockio ([33b3a6d](https://github.com/sudoblockio/tackle/commit/33b3a6d9438e47452f881de3d423683f0f4d2712))

## [0.4.4](https://github.com/robcxyz/tackle/compare/v0.4.3...v0.4.4) (2022-12-03)


### Bug Fixes

* carry call_directory and env through hook calls ([cfe1431](https://github.com/robcxyz/tackle/commit/cfe1431c4031218e4d4273e9e58e2371f789fdc7))
* error parsing multiple args in declarative hook [#106](https://github.com/robcxyz/tackle/issues/106) ([6181275](https://github.com/robcxyz/tackle/commit/6181275184dd0829115becb2957cfca73647b0b4))


### Provider Changes

* add default to listdir path ([30357ce](https://github.com/robcxyz/tackle/commit/30357ce4aa222aa5112407056652222022f60139))
* add glob hook ([1a4b20f](https://github.com/robcxyz/tackle/commit/1a4b20f46c8d9f87b9888e31ccbdc60f6e5b4014))

## [0.4.3](https://github.com/robcxyz/tackle/compare/v0.4.2...v0.4.3) (2022-11-28)


### Bug Fixes

* duplicate hook  to ([4828bb5](https://github.com/robcxyz/tackle/commit/4828bb587996355f0e557af153bdeb637817ab70))
* prompt in  hook ([4bbbd23](https://github.com/robcxyz/tackle/commit/4bbbd23447f4825c468aa169d8dee289961f1e62))


### Refactors

* tackle-box to tackle ([3977a85](https://github.com/robcxyz/tackle/commit/3977a85646fecdcfc4c1d1d15abf3698ea3d9bf3))

## [0.4.2](https://github.com/robcxyz/tackle-box/compare/v0.4.1...v0.4.2) (2022-11-14)


### Bug Fixes

* better excpetion to duplicate values and hacky logic for no_input [#104](https://github.com/robcxyz/tackle-box/issues/104) ([46237f8](https://github.com/robcxyz/tackle-box/commit/46237f8b50bf58126a31df2379844459951c6a0e))
* checkout the right branch with unreleased providers ([ddb790d](https://github.com/robcxyz/tackle-box/commit/ddb790db18d559fff92239ad46798e027a2a23c9))

## [0.4.1](https://github.com/robcxyz/tackle-box/compare/v0.4.0...v0.4.1) (2022-11-14)


### Bug Fixes

* double calling hook with declarative hook field default calling hook ([91f9cd1](https://github.com/robcxyz/tackle-box/commit/91f9cd1cd3b374e174b2e72a173e3743c285a2bd))

## [0.4.0](https://github.com/robcxyz/tackle-box/compare/v0.3.0...v0.4.0) (2022-11-13)


### Features

* add ability to call hooks from declarative hook field defaults ([8e6d503](https://github.com/robcxyz/tackle-box/commit/8e6d5034a2854dcc9938de5cc849970794aa4bbe))
* add ability to print output in yaml/toml/json from CLI ([417526d](https://github.com/robcxyz/tackle-box/commit/417526d2b3f50f4d0c23d6e7b701f99e26671327))
* add help screen for running tackle files ([b054d2b](https://github.com/robcxyz/tackle-box/commit/b054d2bba85cc43574b7eac107bc4471fb2be9d9))
* add hook_dirs field so that tests can import hooks from another directory ([c0b16b2](https://github.com/robcxyz/tackle-box/commit/c0b16b267052295701e52c4874a962cbac3ba7ca))
* allow hooks args and kwargs to be supplied as a param ([a62b4db](https://github.com/robcxyz/tackle-box/commit/a62b4db9cf0d9ed4198a170d0f4e49be520b6bfa))
* segregate hooks into public and private with ability to call them externally by supplying args/kwargs/flags via CLI ([2395f91](https://github.com/robcxyz/tackle-box/commit/2395f915eb463fded962461f348cdf940a5b4417))


### Bug Fixes

* add  in JinjaHook to avoid  error [#90](https://github.com/robcxyz/tackle-box/issues/90) ([ee3b036](https://github.com/robcxyz/tackle-box/commit/ee3b0366393b960f150bd019378f0a4295e5164a))
* install requirements.txt install when there is a ModuleNotFound error on importing a provider's hook ([047f542](https://github.com/robcxyz/tackle-box/commit/047f542d4cfcbbbe6274bfca39099f676e5a8b47))


### Refactors

* field hook tests ([a2eff54](https://github.com/robcxyz/tackle-box/commit/a2eff54dc79f666454021086db5fda80f03f8a8d))


### Provider Changes

* add  hook ([ad5b86b](https://github.com/robcxyz/tackle-box/commit/ad5b86b3374edf72ccfb71f611bec6372d458167))
* add  hook in tackle provider ([40cf028](https://github.com/robcxyz/tackle-box/commit/40cf028fbf8da8affe8b55cf1e56f7c460581271))
* add ability to run tackle hook with args that map to default hooks args ([d1c72d2](https://github.com/robcxyz/tackle-box/commit/d1c72d23674734267ee7dfdeaea76afde8092549))
* add skip_overwrite_files and skip_overwrite_files to generate hook ([95f31b0](https://github.com/robcxyz/tackle-box/commit/95f31b04be8bd07821650d704306241ed8724715))
* add update section hook ([9fac6fb](https://github.com/robcxyz/tackle-box/commit/9fac6fb45425b752232c78762159e487e3029bc6))
* add wip  hook for calling arbitrary CLIs ([2a15c82](https://github.com/robcxyz/tackle-box/commit/2a15c826316d9268a12b51404606b1d9ebcc8141))

## [0.3.0](https://github.com/robcxyz/tackle-box/compare/0.3.0-beta.5...v0.3.0) (2022-08-28)


### Features

* add ability to call declarative hook nested methods ([a44165b](https://github.com/robcxyz/tackle-box/commit/a44165b40b2b1b09ef1d78f1bf3ca1b998a12a0c))
* add auth handler for web requests pprovider ([b635dc3](https://github.com/robcxyz/tackle-box/commit/b635dc3416c2e40b16a3c24f4069179059d43c0d))
* add cleanup function for when we have unquoted strings in hook args which can lead to frustrating errors that are hard to debug ([47871b3](https://github.com/robcxyz/tackle-box/commit/47871b37af14269b305f15d3a00d04eec1d4ac69))
* add datetime provider ([b8b0cfd](https://github.com/robcxyz/tackle-box/commit/b8b0cfd037ea04c8c607de76f059f47df1af2503))
* add default kwargs mapper field so that by default, extra fields can be mapped to another attribute ([94fc9e9](https://github.com/robcxyz/tackle-box/commit/94fc9e952ab511e25af5a25d3281417af852f187))
* add fzf to select hook ([3a295c8](https://github.com/robcxyz/tackle-box/commit/3a295c851268b807f2afff6a92364f28f3c41b0b))
* add override key to cli and main to override input key ([248dbb0](https://github.com/robcxyz/tackle-box/commit/248dbb0f17d4070a2c191f16030a1bd57e0a1384))
* add toml support ([d4698df](https://github.com/robcxyz/tackle-box/commit/d4698dfdfd5999c1cc94a48f314dba3457b0d5a5))
* add xdg and comply with spec to change location of takle directory and add tests for importing ([dd0cccb](https://github.com/robcxyz/tackle-box/commit/dd0cccb078b4a84517338c17340430526e8771ec))
* rm PartialModelMetaclass which simplifies model creation / tmp rm jinja filters ([21b4417](https://github.com/robcxyz/tackle-box/commit/21b441774e0c1fc9038d3583555dbf30e3e3c428))


### Bug Fixes

* drop used hooks from globals to fix second use of hook bug which didn't reinitialize and catch errors better ([f836229](https://github.com/robcxyz/tackle-box/commit/f836229e1e813e00c97e8501f62fe5ad93d9f090))
* error passing context to jinja hook calls ([cfdda49](https://github.com/robcxyz/tackle-box/commit/cfdda495684129623129bc5b8f16cb9d40b43dd9))
* fixture that had invalid validator ([8dbf575](https://github.com/robcxyz/tackle-box/commit/8dbf57573be7eac2a483cfb7056e3f7420150f2b))
* issue with non-defaulted base parameters when calling declarative hook methods ([da315d9](https://github.com/robcxyz/tackle-box/commit/da315d957b7f2ec127395ec87d8ea91d49c6202b))
* issue with unquoted string cleanup function on empty dicts: ([b1e8b3f](https://github.com/robcxyz/tackle-box/commit/b1e8b3faf60c018f143b019f85732b13abe639d2))
* nested declarative hook nested method call ([d9cbf11](https://github.com/robcxyz/tackle-box/commit/d9cbf11b8d0f16dbd115d39f1a798194ca288c2d))
* print in the case of non list / dict outputs ([11ea041](https://github.com/robcxyz/tackle-box/commit/11ea041e5e5c3c8b49e4d0ff8553e8c1dca06033))
* update hook to actually update the values instead of overwriting them ([6a767bc](https://github.com/robcxyz/tackle-box/commit/6a767bc46211727ec55e476101bc862beeef8346))


## [0.3.0-beta](https://github.com/robcxyz/tackle-box/compare/0.3.0-alpha.0...0.3.0-beta.4) (2022-08-28)

### Features

* rm PartialModelMetaclass which simplifies model creation / tmp rm jinja filters ([21b4417](https://github.com/robcxyz/tackle-box/commit/21b441774e0c1fc9038d3583555dbf30e3e3c428))
* add ability for declarative hooks to be run as jinja extensions and filters ([d6e3dea](https://github.com/robcxyz/tackle-box/commit/d6e3dea3fbc1957db7ffc942490b21232ce50a3e))
* add ability to default render context when no hook provided ([0e89c0e](https://github.com/robcxyz/tackle-box/commit/0e89c0eaedb19b7535ec6bf28079fea0f5f18d00))
* add auth handler for web requests pprovider ([b635dc3](https://github.com/robcxyz/tackle-box/commit/b635dc3416c2e40b16a3c24f4069179059d43c0d))
* add basic function parser without exec ([4161410](https://github.com/robcxyz/tackle-box/commit/416141006dc6b84759954f55f18d6b66bd62011d))
* add better exception handling that returns context with the error ([fb0f466](https://github.com/robcxyz/tackle-box/commit/fb0f466c4273d43a3ecbceca0b458c61d799f86e))
* add cleanup function for when we have unquoted strings in hook args which can lead to frustrating errors that are hard to debug ([47871b3](https://github.com/robcxyz/tackle-box/commit/47871b37af14269b305f15d3a00d04eec1d4ac69))
* add datetime provider ([b8b0cfd](https://github.com/robcxyz/tackle-box/commit/b8b0cfd037ea04c8c607de76f059f47df1af2503))
* add find-in-parent cli flag and in tackle to search for tackle file in parent ([daee9d2](https://github.com/robcxyz/tackle-box/commit/daee9d2b24bc591ed73eebfca129477563af1af9))
* add fzf to select hook ([3a295c8](https://github.com/robcxyz/tackle-box/commit/3a295c851268b807f2afff6a92364f28f3c41b0b))
* add implicit value for an empty tackle call - searching for nearest tackle ([c5dd034](https://github.com/robcxyz/tackle-box/commit/c5dd0343f98b981852ea56f6c5861b29989b0f97))
* add latest flag to pull latest version ([8c3b687](https://github.com/robcxyz/tackle-box/commit/8c3b6874805a4cf08af5cab169fbc9a50f617aaf))
* add mkdocs and first pass on documentation ([be92f89](https://github.com/robcxyz/tackle-box/commit/be92f8902a038b16dd7d8d5b11c17e76a0878384))
* add override key to cli and main to override input key ([248dbb0](https://github.com/robcxyz/tackle-box/commit/248dbb0f17d4070a2c191f16030a1bd57e0a1384))
* add provider docs hook and docs code generator ([2befdc5](https://github.com/robcxyz/tackle-box/commit/2befdc5542d4fe6ecdadd601d3b269e734413cbd))
* add toml support ([d4698df](https://github.com/robcxyz/tackle-box/commit/d4698dfdfd5999c1cc94a48f314dba3457b0d5a5))
* add try method without any except ([6c33dbc](https://github.com/robcxyz/tackle-box/commit/6c33dbcf5a8f93abb97dd59b06be626230498fd2))
* add xdg and comply with spec to change location of takle directory and add tests for importing ([dd0cccb](https://github.com/robcxyz/tackle-box/commit/dd0cccb078b4a84517338c17340430526e8771ec))
* get else and except working and fix out of order macros ([9f018e2](https://github.com/robcxyz/tackle-box/commit/9f018e2ffc85872c6f95e7bfaf57bc359a73fe7f))
* implement initial hook methods ([67cf309](https://github.com/robcxyz/tackle-box/commit/67cf30946a2e6f3f7b024a28c1753245e43a939f))
* implement memory maangement with public private temp and existing contexts ([b37392e](https://github.com/robcxyz/tackle-box/commit/b37392eeb1d0153809b00adbcf8ee7a89d322e6a))
* implement methods on declarative hooks ([60f620f](https://github.com/robcxyz/tackle-box/commit/60f620f3486b98a9eb7b319e78cdd9bec7c39426))
* initial collections provider ([ffcd272](https://github.com/robcxyz/tackle-box/commit/ffcd2726b11fe7481f16e6db9dfd549bb55ebb42))
* make parser generic - mid overhaul ([6fbda6a](https://github.com/robcxyz/tackle-box/commit/6fbda6aa1b930f9ec10db7805543a174202f45c5))
* new parsing order logic and hook syntax ([91e37cd](https://github.com/robcxyz/tackle-box/commit/91e37cd91d4a6c3c81c615a44d9ac387344684dd))
* provider overhaul for 0.3.0 release ([070caaa](https://github.com/robcxyz/tackle-box/commit/070caaab3989e674202fa0102e804fe7029b5281))
* **README:** added cookiecutter-django-rest ([f173ef6](https://github.com/robcxyz/tackle-box/commit/f173ef6818d179ed4f21ef899cad49bcb080b9f3))
* **README:** added cookiecutter-es6-boilerplate ([dc533d4](https://github.com/robcxyz/tackle-box/commit/dc533d4db6c7f2ff54f0b8549bc982659d83e075))
* redo rendering to include special vars lazy lookup and remove slugify extension ([8ebf200](https://github.com/robcxyz/tackle-box/commit/8ebf200b7edfbbf4f983d0490b439aea78d3f99b))
* remove pre hook init object (hook_dict) and get loops working ([1fab36c](https://github.com/robcxyz/tackle-box/commit/1fab36c197ed71997d1f743b206b5f15215147e9))
* rm click dependency and use argparse ([60b98e6](https://github.com/robcxyz/tackle-box/commit/60b98e6f4f00de706f42c798b22d295a1fc3abf7))
* update all system hooks with descriptions and arguments ([ac56486](https://github.com/robcxyz/tackle-box/commit/ac5648638775a90e010ae18013ff8d47eacfd091))
* update parser to render variables more selectively and before they are used to initialize a hook ([1b160ca](https://github.com/robcxyz/tackle-box/commit/1b160ca852644e1118071eafbadac0ac9f6174b1))
* upgrade PyInquirer to InquirerPy ([62b68e4](https://github.com/robcxyz/tackle-box/commit/62b68e43562163aa2715c6e03b40ea973af0313e))

### Bug Fixes

* issue with non-defaulted base parameters when calling declarative hook methods ([da315d9](https://github.com/robcxyz/tackle-box/commit/da315d957b7f2ec127395ec87d8ea91d49c6202b))
* issue with unquoted string cleanup function on empty dicts: ([b1e8b3f](https://github.com/robcxyz/tackle-box/commit/b1e8b3faf60c018f143b019f85732b13abe639d2))
* add exception for unknown variables the same as hook_types closes [#55](https://github.com/robcxyz/tackle-box/issues/55) ([b0b47ea](https://github.com/robcxyz/tackle-box/commit/b0b47ea85ae9be3ceeb96149126f15261b1cbc2c))
* add field for functions ([1a56f74](https://github.com/robcxyz/tackle-box/commit/1a56f74c81136394b29d041e49c9ae9d23d735aa))
* add smart_union to fix mangling of list inputs ([971ca88](https://github.com/robcxyz/tackle-box/commit/971ca882371f7079fc5f3f7a893bf6116b0d90f4))
* args refactor in docs hook ([0163d99](https://github.com/robcxyz/tackle-box/commit/0163d993a31ae65237ae76f1d2e4b565ba4c682c))
* checkbox hook with new API ([6e0b532](https://github.com/robcxyz/tackle-box/commit/6e0b532e54a08de49468979971013d177ce363f3))
* compact expression macro reindex based on key_path_block correctly ([a53942a](https://github.com/robcxyz/tackle-box/commit/a53942ab1fccccba52e93d4d550c0733bc145ee5))
* compact key macro to preserve order ([7ecf467](https://github.com/robcxyz/tackle-box/commit/7ecf467f0507bb91869a2846abdfb8eb210ce73c))
* declarative hooks using base object types and validations ([a3aa32d](https://github.com/robcxyz/tackle-box/commit/a3aa32db5bd2da67b2e2afe06977b50768f783c7))
* distinguish types with merge ([6c3bbed](https://github.com/robcxyz/tackle-box/commit/6c3bbedebd574cbafc26b2a058d175c6193c75b1))
* docs gen problem hooks copy over ([ff2a7f8](https://github.com/robcxyz/tackle-box/commit/ff2a7f8f32ff7f8122462e2dd3263747447649e1))
* drop used hooks from globals to fix second use of hook bug which didn't reinitialize and catch errors better ([f836229](https://github.com/robcxyz/tackle-box/commit/f836229e1e813e00c97e8501f62fe5ad93d9f090))
* else condition with bools, ints, and floats ([c2ce7b4](https://github.com/robcxyz/tackle-box/commit/c2ce7b42fe4c0f868f6ddae30963ef52e6a80968))
* embedded blocks issue with copying over key_path ([00f7ce8](https://github.com/robcxyz/tackle-box/commit/00f7ce8fdb356e8350d2c81cc75ee7b5c236b3cf))
* extends in declarative hooks ([8b33e6c](https://github.com/robcxyz/tackle-box/commit/8b33e6c1f9eff7d5b81c661eacc5af2c0681c72b))
* fixture that had invalid validator ([8dbf575](https://github.com/robcxyz/tackle-box/commit/8dbf57573be7eac2a483cfb7056e3f7420150f2b))
* for checkbox hook return all when checked and no_input ([a659901](https://github.com/robcxyz/tackle-box/commit/a6599014ad499085c18db5eb8504d8a3bec6457a))
* for temporary contexts which in edge cases can have unusable single values written them ([003563e](https://github.com/robcxyz/tackle-box/commit/003563ecd29c4ee8c4d8a01bf1b99c85ae886094))
* function return ref ([8265151](https://github.com/robcxyz/tackle-box/commit/8265151491728e78ae3aaf5e53ce43a583fad655))
* keyboard interrupt handling in prompts ([fe112d0](https://github.com/robcxyz/tackle-box/commit/fe112d0c90bd4ee3c1a3921604d22d4e4e3c15c3))
* load context on tackle hook with right precedence ([760cb61](https://github.com/robcxyz/tackle-box/commit/760cb61a27c0ffa523dd9e2eb7815a3881507bdd))
* match hook block macro not indenting block matches properly ([12cfc55](https://github.com/robcxyz/tackle-box/commit/12cfc554f2367147f895ce01df5126cc04274187))
* merge dict in block ([ec8d3d9](https://github.com/robcxyz/tackle-box/commit/ec8d3d9d39738e102195ba707da5098bc4575c1c))
* move try back into parser so it doesn't automatically write None to output - only on except ([797c776](https://github.com/robcxyz/tackle-box/commit/797c7768b83b5babe917ba23054415cdd0c9ed3b))
* parsing error from ruamel fix macro on empty items ([1e460b9](https://github.com/robcxyz/tackle-box/commit/1e460b98f1b794ed25221fd4f76fce264fa2913f))
* print in the case of non list / dict outputs ([11ea041](https://github.com/robcxyz/tackle-box/commit/11ea041e5e5c3c8b49e4d0ff8553e8c1dca06033))
* readable key path for prompt messages ([9bfaa7f](https://github.com/robcxyz/tackle-box/commit/9bfaa7f5419651a3170574a5059153ac36175e99))
* readable key path for string ([6ee040e](https://github.com/robcxyz/tackle-box/commit/6ee040ebcc9233210be9c2ea414283be6928851f))
* rebuild block hook indexing so that writes happen directly to output_dict ([874a046](https://github.com/robcxyz/tackle-box/commit/874a0469b91db94d07f0f86344f27beaf89b57b6))
* remove choices and default args from prompt hooks - only message now ([ca135dd](https://github.com/robcxyz/tackle-box/commit/ca135dd40a0a82cdbe92ef9012f5791af042fb70))
* ruamel parsing error macro that messed up empty keys ([c6bc582](https://github.com/robcxyz/tackle-box/commit/c6bc58202e2fde7bddf62587c1362944f80573ba))
* ruamel parsing error with un-quoted braces that returns ambiguous ordered dict and jams parser ([bd6922f](https://github.com/robcxyz/tackle-box/commit/bd6922fe24564f461eac87c4d7a7d30a4738dc88))
* update hook to actually update the values instead of overwriting them ([6a767bc](https://github.com/robcxyz/tackle-box/commit/6a767bc46211727ec55e476101bc862beeef8346))
* warning about invalid escape of \, in command lexer ([6849824](https://github.com/robcxyz/tackle-box/commit/684982491e194b96d4e00a97bafb5594813a8a08))
* yaml hook - force output to be string with extra json [#56](https://github.com/robcxyz/tackle-box/issues/56) ([80a956f](https://github.com/robcxyz/tackle-box/commit/80a956fd6a6f5564dfe7433515fd587503cbf20e))
