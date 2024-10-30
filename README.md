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

| Prefix `import` or `from` | Description                                   |
| ------------------------- | --------------------------------------------- |
| `template`                | Creates templates OWL.                        |
| `component`               | Creates an import for OWL components in Odoo. |
| `will`                    | Imports OWL component lifecycle methods.      |
| `registry`                | Imports the OWL registry.                     |
| `translate`               | Imports the OWL translation function.         |
| `memoize`                 | Imports the memoize function.                 |
| `browser`                 | Imports the OWL browser utility.              |
| `lifecyle-hooks`          | Imports lifecycle hooks.                      |
| `other-hooks`             | Imports Utils hooks.                          |
| `hooks-owst`              | onWillStart hook for async setup.             |
| `hooks-owr`               | onWillRender hook for pre-render actions.     |
| `hooks-or`                | onRendered hook for post-render actions.      |
| `hooks-omt`               | onMounted hook for component mount actions.   |
| `hooks-oup`               | onWillUpdateProps hook for prop updates.      |
| `hooks-owp`               | onWillPatch hook before DOM patching.         |
| `hooks-op`                | onPatched hook after DOM patching.            |
| `hooks-owum`              | onWillUnmount hook before component unmounts. |
| `hooks-owdt`              | onWillDestroy hook before component cleanup.  |
| `hooks-oe`                | onError hook for error handling.              |
| `.....................`   | ....................                          |

</details>

```javascript
/** @odoo-module */,
import { Component } from '@odoo/owl';,
import { registry } from '@web/core/registry;',
import { standardFieldProps } from '@web/views/fields/standard_field_props';,
class SideBar extends Component {
  static template = 'MODULE.TEMPLATE_NAME'
  static props = {...standardFieldProps};
  static defaultProps = {};
  setup() {

  }
}
registry.category('actions').add('module.c_name', MyComponents),
registry.category('views').add('module.c_name', MyComponents),
registry.category('services').add('module.c_name', MyComponents)
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
