# Installed packages (via pip)
from django.template import Context, Template
import pkg_resources

# Edx dependencies
from xblock.core import XBlock
from xblock.fields import Integer, Boolean, Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

# Make '_' a no-op so we can scrape strings
_ = lambda text: text


class EolDialogsXBlock(StudioEditableXBlockMixin, XBlock):

    display_name = String(
        display_name=_("Display Name"),
        help=_("Display name for this module"),
        default="Eol Dialogs XBlock",
        scope=Scope.settings,
    )

    icon_class = String(
        default="other",
        scope=Scope.settings,
    )

    image_url = String(
        display_name=_("URL del personaje"),
        help=_("Indica la URL a la imagen del personaje en el dialogo"),
        default="https://static.sumaysigue.uchile.cl/cmmeduformacion/produccion/assets/img/diag_aldo.png",
        scope=Scope.settings,
    )

    image_size = Integer(
        display_name=_("tamaño del personaje"),
        help=_("(Solo en REDFID)"),
        default=112,
        scope=Scope.settings,
    )

    flip_image = Boolean(
        display_name=_('Invertir personaje'),
        help=_('Invertir imagen del personaje'),
        default=False,
        scope=Scope.settings,
    )

    background_color = String(
        display_name=_("Color de fondo"),
        help=_("Color del contenedor del dialogo"),
        default="#F8E37B",
        scope=Scope.settings,
    )

    border_color = String(
        display_name=_("Color del borde"),
        help=_("Color del borde del contenedor del dialogo"),
        default="#F8E37B",
        scope=Scope.settings,
    )

    text_color = String(
        display_name=_("Color del texto"),
        help=_("Color del texto del dialogo"),
        default="#000000",
        scope=Scope.settings,
    )

    side = String(
        display_name = _("Posicion"),
        help = _("Indica la posicion del dialogo"),
        default = "Izquierda",
        values = ["Izquierda", "Derecha"],
        scope = Scope.settings
    )

    character_name = String(
        display_name=_("Nombre del personaje (RedFid)"),
        help=_("Solo disponible en RedFid"),
        default="Firulais",
        scope=Scope.settings,
    )

    text = String(
        display_name=_("Contenido del dialogo"), 
        multiline_editor='html', 
        resettable_editor=False,
        default=_("<p>Contenido del dialogo.</p>"), 
        scope=Scope.settings,
        help=_("Indica el contenido del dialogo")
    )

    theme = String(
        display_name = _("Estilo"),
        help = _("Cambiar estilo de la pregunta"),
        default = "SumaySigue",
        values = ["SumaySigue", "Media","RedFid"],
        scope = Scope.settings
    )

    globo = String(
        display_name = _("globo"),
        help = _("Cambiar tipo de globo de dialogo (solo SumaySigue)"),
        default = "dialogo",
        values = ["dialogo", "pensamiento"],
        scope = Scope.settings
    )

    editable_fields = ('display_name', 'image_url', 'image_size', 'flip_image', 'background_color','border_color', 'text_color', 'side', 'character_name', 'text', 'theme','globo')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        context_html = self.get_context()
        template = self.render_template('static/html/eoldialogs.html', context_html)
        frag = Fragment(template)
        frag.add_css(self.resource_string("static/css/eoldialogs.css"))
        frag.add_javascript(self.resource_string("static/js/src/eoldialogs.js"))
        settings = {
            'location'  : str(self.location).split('@')[-1]
        }
        frag.initialize_js('EolDialogsXBlock', json_args=settings)
        return frag

    def get_context(self):
        return {
            'xblock': self,
            'location': str(self.location).split('@')[-1]
        }

    def render_template(self, template_path, context):
        template_str = self.resource_string(template_path)
        template = Template(template_str)
        return template.render(Context(context))
    
        # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("EolDialogsXBlock",
             """<eoldialogs/>
             """),
            ("Multiple EolDialogsXBlock",
             """<vertical_demo>
                <eoldialogs
                theme='Media'
                image_url = 'https://static.sumaysigue.uchile.cl/SySMedia/produccion/EPI/T01/A01/img/juanr.png'
                />
                <eoldialogs
                theme='Media'
                image_url = 'https://static.sumaysigue.uchile.cl/SySMedia/produccion/EPI/T01/A01/img/juanr.png'
                side = 'Derecha'
                />
                <eoldialogs/>
                <eoldialogs/>
                </vertical_demo>
             """),
        ]
