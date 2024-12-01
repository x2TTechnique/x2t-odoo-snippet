<div style="border: 2px solid #000; padding: 16px; border-radius: 8px;">

## 📢 **Important Announcement**

Starting from **Odoo 18**, we will align the versioning of our snippets with the respective Odoo version.  
This change is made to help you easily select the appropriate snippets for the version of Odoo you are currently using.

Please ensure you choose the snippets that match your Odoo version to avoid compatibility issues.

Thank you for your understanding and support! 🙌

Best regards,  
**Bùi Đức Tuấn**

</div>

---

# VS Code Snippets for Odoo Development

This repository provides a collection of VS Code snippets for efficient Odoo development in JavaScript, XML, and Python. The snippets are designed to help developers quickly generate common code structures and components.

# Usage

## Javascript

<details>

| Prefix                | Description    |
| --------------------- | -------------- |
| `console` or `log`    | Console log.   |
| `function`            | Function.      |
| `function` or `arrow` | Arow Function. |

---

| Prefix `import` or `from` | Description                                                                    |
| ------------------------- | ------------------------------------------------------------------------------ |
| `console` or `log`        | Console log.                                                                   |
| `function`                | Function declaration in JavaScript.                                            |
| `arrow` or `function`     | Arrow function syntax in JavaScript.                                           |
| `import` or `from`        | Import statements for modules in JavaScript.                                   |
| `template`                | Creates templates for OWL components in Odoo.                                  |
| `component`               | Imports OWL component in Odoo for development.                                 |
| `will`                    | Imports OWL component lifecycle methods.                                       |
| `registry`                | Imports the OWL registry for managing components.                              |
| `translate`               | Imports the translation function in OWL for localization.                      |
| `memoize`                 | Imports the memoization function for optimized calculations.                   |
| `browser`                 | Imports the OWL browser utility for web interactions.                          |
| `lifecyle-hooks`          | Imports lifecycle hooks for OWL components (e.g., `onWillStart`, `onMounted`). |
| `other-hooks`             | Imports other utility hooks from OWL (e.g., `useState`, `useEffect`).          |
| `onWillStart`             | `onWillStart` hook for asynchronous setup in OWL.                              |
| `onWillRender`            | `onWillRender` hook for actions before rendering in OWL.                       |
| `onRendered`              | `onRendered` hook for actions after rendering in OWL.                          |
| `onMounted`               | `onMounted` hook for actions after mounting a component in OWL.                |
| `onWillUpdateProps`       | `onWillUpdateProps` hook for updating component props in OWL.                  |
| `onWillPatch`             | `onWillPatch` hook for actions before DOM patching in OWL.                     |
| `onPatched`               | `onPatched` hook for actions after DOM patching in OWL.                        |
| `onWillUnmount`           | `onWillUnmount` hook for cleanup before component unmount in OWL.              |
| `onWillDestroy`           | `onWillDestroy` hook for cleanup before component destruction in OWL.          |
| `onError`                 | `onError` hook for handling errors in OWL.                                     |
| `manifest`                | Creates Odoo manifest file for module definition.                              |
| `init`                    | Creates the `__init__.py` for module initialization in Odoo.                   |
| `class` or `model`        | Odoo model class template for defining models.                                 |
| `create` or `def`         | Creates ORM functions in Odoo models.                                          |
| `depends`                 | Adds the `depends` decorator for model dependencies in Odoo.                   |
| `onchange`                | Adds the `@onchange` decorator for fields in Odoo models.                      |
| `field` or `char`         | Creates `Char` field in Odoo models.                                           |
| `form` or `view`          | Defines views like form, tree, kanban, etc., in Odoo XML.                      |
| `action`                  | Creates actions such as window, client, or server actions in Odoo XML.         |

</details>

```javascript
/** @odoo-module */,
import { Component } from '@odoo/owl';,
import { registry } from '@web/core/registry;',
import { standardFieldProps } from '@web/views/fields/standard_field_props';
class SideBar extends Component {
static template = 'MODULE.TEMPLATE_NAME'
static props = {...standardFieldProps};
static defaultProps = {};
setup() {

}
}
registry.category('actions').add('', SideBar),
registry.category('views').add('', SideBar),
registry.category('services').add('', SideBar)
```

## Python

<details>

| Prefix             | Description                       |
| ------------------ | --------------------------------- |
| `manifest`         | Odoo import manifest content      |
| `init`             | Odoo import manifest content.     |
| `class` or `model` | Odoo import model class template. |
| `create` or `def`  | ORM Function.                     |
| `depends`          | Depends Decoration.               |
| `onchange`         | Onchange Decoration.              |
| `field` or `char`  | Char field.                       |

</details>

Examples: `field` or `char`

```python
foo = fields.Char(,
    string='Foo',,
    default='Foo',,
    required=False,
    readonly=False,
    index=False, # [('True' or'btree'), 'btree_not_null', 'trigram', ('None' or 'False')],
    groups='base.group_user',
    company_dependent=False,
    coppy=False,
)
```

## XML

<details>

| Prefix                  | Description                                      |
| ----------------------- | ------------------------------------------------ |
| `form` or `view`        | Odoo import view ['form','tree','kanban',...]    |
| `action`                | Odoo import action ['window','client', 'server'] |
| `.....................` | ....................                             |

</details>

Examples: `form`

```xml
<record id='view_MODEL_NAME_form' model='ir.ui.view'>
<field name='name'></field>
<field name='model'></field>
<field name='arch' type='xml'>
    <form string='' create='' edit='' duplicate='' delete='' js_class='' disable_autofocus='1' banner_route='/module/banner'>
        <sheet>
            <group>
                <group>
                    <field name='' widget='' options='{}'/>
                </group>
                <group>
                </group>
                </group>
                <notebook>
                    <page>
                        <group>
                            <group>
                                <field name='' widget='' options='{}'/>
                            </group>
                            <group>
                            </group>
                        </group>
                    </page>
                </notebook>
        </sheet>
        <div class='oe_chatter'>
            <field name='message_follower_ids' widget='mail_followers' />
            <field name='activity_ids' widget='mail_activity' />
            <field name='message_ids' widget='mail_thread' />
        </div>
    </form>
</field>
</record>
```
