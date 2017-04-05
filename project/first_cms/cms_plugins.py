from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ContactUSModel
from django.utils.translation import ugettext as _


class ContactUsPluginPublisher(CMSPluginBase):
    model = ContactUSModel  # model where plugin data are saved
    module = _("ContactUs")
    name = _("Contact Us")  # name of the plugin in the interface
    render_template = "first_cms/base.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(ContactUsPluginPublisher)  # register the plugin