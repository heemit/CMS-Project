from django.forms               import widgets
from django.utils.safestring    import mark_safe

class GrapeJSWidget(widgets.Textarea):
    class Media:
        css = {
            'all': [
                'grapesjs/css/grapes.min.css',
                #'https://unpkg.com/grapesjs/dist/css/grapesjs-preset-webpage.min.css',
                'grapesjs/css/grapick.min.css',
                'grapesjs/fonts/all.min.css',
            ]
        }
        js = [
            'grapesjs/js/grapes.min.js',
            'grapesjs/js/grapesjs-preset-webpage.js',
            'grapesjs/js/grapesjs-blocks-basic.min.js',
            'grapesjs/js/grapesjs-plugin-forms.js',
            'grapesjs/js/grapesjs-component-countdown.js',
            'grapesjs/js/grapesjs-plugin-export.js',
            'grapesjs/js/grapesjs-tabs.min.js',
            'grapesjs/js/grapesjs-custom-code.js',
            'grapesjs/js/grapesjs-touch.min.js',
            'grapesjs/js/grapesjs-parser-postcss.min.js',
            'grapesjs/js/grapesjs-tooltip.js',
            'grapesjs/js/grapesjs-tui-image-editor.min.js',
            'grapesjs/js/grapesjs-typed.js',
            'grapesjs/js/grapesjs-style-bg.js',
            'grapesjs/js/grapesjs-style-gradient.js',
            #'grapesjs/js/grapesjs-preset-newsletter.js',
            'grapesjs/js/grapick.min.js',
        ]

    def __init__(self, *args, css_files=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.css_files = css_files or []

    def render(self, name, value, attrs=None, renderer=None):
        # Render the textarea for GrapeJS
        value = value or ''
        html = f'<textarea name="{name}" hidden>{value if value else ""}</textarea>'

        # Generate custom CSS links
        custom_css_links = ''.join(
            f'<link rel="stylesheet" href="{css}" type="text/css">' for css in self.css_files
        )

        # Add GrapeJS initialization script with plugins and CSS
        grapejs_script = f"""
        <div id="gjs-container-{name}" style="height: 500px; border: 1px solid #ddd; margin-top: 10px;"></div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                var existingContent = `{value.strip()}`;

                var editor = grapesjs.init({{
                    container: '#gjs-container-{name}',
                    height: '80vh',
                    fromElement: false,
                    showOffsets: true,
                    allowScripts: true,
                    noticeOnUnload: false,
                    clearOnRender: false,
                    dragMode: 'absolute',
                    storageManager: {{
                        type: 'none',
                    }},
                    assetManager: {{
                        embedAsBase64: true,
                        assets: [],
                    }},
                    selectorManager: {{ componentFirst: true }},
                    canvas: {{
                        styles: ['body {{ overflow: auto; }}'],
                        scroll: true,
                    }},
                    styleManager: {{
                        sectors: [
                            {{
                                name: 'General',
                                open: true,
                                properties: [
                                    'width', 'min-height', 'margin', 'padding', 'display', 'position',
                                    'top', 'right', 'bottom', 'left', 'z-index'
                                ],
                            }},
                            {{
                                name: 'Layout',
                                open: true,
                                properties: [
                                    'display', 'position', 'float', 'clear', 'width', 'height', 'top',
                                    'left', 'right', 'bottom',
                                ]
                            }},
                            {{
                                name: 'Typography',
                                properties: [
                                    'font-family', 'font-size', 'font-weight', 'color', 'letter-spacing',
                                    'line-height', 'text-align', 'text-shadow',
                                ],
                            }},
                            {{
                                name: 'Decorations',
                                open: true,
                                properties: [
                                    'width', 'height', 'background', 'border', 'box-shadow', 'border-radius'
                                ],
                            }},
                        ],
                    }},
                    plugins: [
                        'gjs-blocks-basic',
                        'grapesjs-plugin-forms',
                        'grapesjs-component-countdown',
                        'grapesjs-plugin-export',
                        'grapesjs-tabs',
                        'grapesjs-custom-code',
                        'grapesjs-touch',
                        'grapesjs-parser-postcss',
                        'grapesjs-tooltip',
                        'grapesjs-tui-image-editor',
                        'grapesjs-typed',
                        'grapesjs-style-bg',
                        'grapesjs-preset-webpage',
                        'grapesjs-preset-newsletter',
                    ],
                    pluginsOpts: {{
                        'gjs-blocks-basic': {{ flexGrid: true }},
                        'grapesjs-preset-webpage': {{
                            modalImportTitle: 'Import Template',
                            modalImportLabel: '<div>Paste your HTML/CSS and click Import</div>',
                            modalImportContent: function(editor) {{
                                return editor.getHtml() + '<style>' + editor.getCss() + '</style>';
                            }},
                        }},
                        'grapesjs-tooltip': {{
                            tooltipBgColor: '#333',
                            tooltipColor: '#fff',
                        }},
                    }},
                    resizable: true,
                }});

                if (existingContent) {{
                    editor.setComponents(existingContent);
                }}

                // Inject custom CSS files into the GrapeJS iframe
                var customCssFiles = {self.css_files};
                editor.on('load', function() {{
                    var iframe = editor.Canvas.getFrameEl();
                    var head = iframe.contentDocument.head;
                    customCssFiles.forEach(function(cssFile) {{
                        var link = document.createElement('link');
                        link.rel = 'stylesheet';
                        link.href = cssFile;
                        head.appendChild(link);
                    }});
                }});

                // Update the textarea value on changes in GrapeJS editor
                editor.on('update', () => {{
                    document.querySelector('[name="{name}"]').value = editor.getHtml();
                }});

                // Predefined Templates
                editor.BlockManager.add('header-template', {{
                    label: 'Header Template',
                    content: '<header><h1>My Website Header</h1></header>',
                }});
                editor.BlockManager.add('footer-template', {{
                    label: 'Footer Template',
                    content: '<footer><p>&copy; 2025 My Website Footer</p></footer>',
                }});
                editor.BlockManager.add('landing-template', {{
                    label: 'Landing Page Template',
                    content: '<section class="landing-page"><h1>Welcome to My Website</h1><p>Great content goes here</p></section>',
                }});

            }});
        </script>
        """
        return mark_safe(html + custom_css_links + grapejs_script)
