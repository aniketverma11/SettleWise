import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from admin_interface.models import Theme

def setup_theme():
    theme, created = Theme.objects.get_or_create(name='Django', defaults={'active': True})
    
    # SettleWise Colors
    primary_color = '#002244'  # Deep Navy
    secondary_color = '#10b981' # Emerald Green
    
    theme.set_active()
    theme.title = 'SettleWise Admin'
    theme.logo = 'logo.png'
    
    # Colors
    theme.css_header_background_color = primary_color
    theme.css_header_link_color = '#FFFFFF'
    theme.css_header_link_hover_color = secondary_color
    
    theme.css_module_background_color = primary_color
    theme.css_module_text_color = '#FFFFFF'
    theme.css_module_link_color = '#FFFFFF'
    theme.css_module_link_hover_color = secondary_color
    
    theme.css_generic_link_color = primary_color
    theme.css_generic_link_hover_color = secondary_color
    
    theme.css_save_button_background_color = secondary_color
    theme.css_save_button_background_hover_color = '#059669' # Darker emerald
    theme.css_save_button_text_color = '#FFFFFF'
    
    theme.css_delete_button_background_color = '#CC0000'
    theme.css_delete_button_background_hover_color = '#990000'
    theme.css_delete_button_text_color = '#FFFFFF'
    
    theme.save()
    print(f"Theme '{theme.name}' updated with SettleWise colors.")

if __name__ == "__main__":
    setup_theme()
