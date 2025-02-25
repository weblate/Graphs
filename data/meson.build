# SPDX-License-Identifier: GPL-3.0-or-later
desktop_file_in = configure_file(
        input: application_id + '.desktop.in.in',
       output: application_id + '.desktop.in',
configuration: conf
)

desktop_file = i18n.merge_file(
        input: desktop_file_in,
       output: application_id + '.desktop',
         type: 'desktop',
       po_dir: '../po',
      install: true,
  install_dir: join_paths(datadir, 'applications')
)

desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils, args: [desktop_file])
endif

appstream_file_in = configure_file(
        input: application_id + '.appdata.xml.in.in',
       output: application_id + '.appdata.xml.in',
configuration: conf
)

appstream_file = i18n.merge_file(
        input: appstream_file_in,
       output: application_id + '.appdata.xml',
       po_dir: '../po',
      install: true,
  install_dir: join_paths(datadir, 'appdata')
)

appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util, args: ['validate', appstream_file])
endif

install_data(application_id + '.gschema.xml',
  install_dir: join_paths(datadir, 'glib-2.0/schemas'),
 install_mode: 'rwxrwxrwx'
)

compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file',
       compile_schemas,
       args: ['--strict', '--dry-run', meson.current_source_dir()])
endif

blueprints = custom_target('blueprints',
  input: files(
    'ui/add_equation_window.blp',
    'ui/add_style.blp',
    'ui/dialogs.blp',
    'ui/edit_item.blp',
    'ui/export_figure.blp',
    'ui/figure_settings.blp',
    'ui/import.blp',
    'ui/help_overlay.blp',
    'ui/item_box.blp',
    'ui/preferences.blp',
    'ui/style_box.blp',
    'ui/style_color_box.blp',
    'ui/style_window.blp',
    'ui/transform_window.blp',
    'ui/window.blp'
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

resources = gnome.compile_resources(
  application_id,
  application_id + '.gresource.xml',
    dependencies: blueprints,
gresource_bundle: true,
      source_dir: meson.current_build_dir(),
         install: true,
     install_dir: pkgdatadir,
)

scalable_dir = join_paths('icons', 'hicolor', 'scalable', 'apps')
icon_name = ('@0@.svg').format(application_id)
if debug
  icon_name = ('@0@.Devel.svg').format(application_id)
endif
install_data(
  join_paths(scalable_dir, icon_name),
     rename: ('@0@.svg').format(application_id),
install_dir: join_paths(datadir, scalable_dir)
)

symbolic_dir = join_paths('icons', 'hicolor', 'symbolic', 'apps')
install_data(
  join_paths(symbolic_dir, ('@0@-symbolic.svg').format(application_id)),
  install_dir: join_paths(datadir, symbolic_dir)
)
