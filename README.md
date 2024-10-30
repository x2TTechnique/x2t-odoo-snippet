# VS Code Snippets for Odoo Development

This repository provides a collection of VS Code snippets for efficient Odoo development in JavaScript, XML, and Python. The snippets are designed to help developers quickly generate common code structures and components.

# Usage

## Javascript

<details>

| Prefix | Description    |
| ------ | -------------- |
| `cl`   | Console log.   |
| `f`    | Function.      |
| `af`   | Arow Function. |

| Prefix                     | Description                                   |
| -------------------------- | --------------------------------------------- |
| `o-template` or `template` | Creates templates OWL.                        |
| `oi-component`             | Creates an import for OWL components in Odoo. |
| `oi-lifecyle`              | Imports OWL component lifecycle methods.      |
| `oi-registry`              | Imports the OWL registry.                     |
| `oi-translate`             | Imports the OWL translation function.         |
| `oi-memoize`               | Imports the memoize function.                 |
| `oi-browser`               | Imports the OWL browser utility.              |
| `oi-lifecyle-hooks`        | Imports lifecycle hooks.                      |
| `oi-other-hooks`           | Imports Utils hooks.                          |
| `oi-hooks-owst`            | onWillStart hook for async setup.             |
| `oi-hooks-owr`             | onWillRender hook for pre-render actions.     |
| `oi-hooks-or`              | onRendered hook for post-render actions.      |
| `oi-hooks-omt`             | onMounted hook for component mount actions.   |
| `oi-hooks-oup`             | onWillUpdateProps hook for prop updates.      |
| `oi-hooks-owp`             | onWillPatch hook before DOM patching.         |
| `oi-hooks-op`              | onPatched hook after DOM patching.            |
| `oi-hooks-owum`            | onWillUnmount hook before component unmounts. |
| `oi-hooks-owdt`            | onWillDestroy hook before component cleanup.  |
| `oi-hooks-oe`              | onError hook for error handling.              |
| `.....................`    | ....................                          |

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

| Prefix                            | Description                           |
| --------------------------------- | ------------------------------------- |
| `oi-manifest`                     | Odoo import manifest content          |
| `oi-init`                         | Odoo import manifest content.         |
| `oi-class-model`                  | Odoo import model class template.     |
| `oi-class-transient`              | Odoo import model transient template. |
| `oi-class-abtract`                | Odoo import model abtract template.   |
| `oi-method-{create,write,unlink}` | Create function.                      |
| `oi-method-compute-display-name`  | Display name function.                |
| `oi-depends`                      | Depends Decoration.                   |
| `oi-onchange`                     | Onchange Decoration.                  |
| `oi-field-char`                   | Char field.                           |
| `oi-field-boolean`                | Boolean field.                        |
| `oi-field-integer`                | Integer field.                        |
| `oi-field-float`                  | Float field.                          |
| `oi-field-binary`                 | Binary field.                         |
| `oi-field-html`                   | HTMl field.                           |
| `oi-field-image`                  | Image field.                          |
| `oi-field-monetary`               | Monetary field.                       |
| `oi-field-selection`              | Selection field.                      |
| `oi-field-add-selection`          | Add Selection field.                  |
| `oi-field-text`                   | Text field.                           |
| `oi-field-m2o`                    | Many2one field.                       |
| `oi-field-o2m`                    | One2many field.                       |
| `oi-field-m2m`                    | Many2many field.                      |
| `oi-field-reference`              | Reference field.                      |
| `oi-field-m2o-reference`          | Many2oneReference field.              |
| `oi-field-m2o-related`            | Related field.                        |
| `.....................`           | ....................                  |

</details>

Examples: `oi-field-char`

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
| `oi-view-*`             | Odoo import view ['form','tree','kanban',...]    |
| `oi-action-*`           | Odoo import action ['window','client', 'server'] |
| `.....................` | ....................                             |

</details>

Examples: `oi-view-form`

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

## CSV

<details>

| Prefix    | Description     |
| --------- | --------------- |
| `oi-odoo` | Odoo import CSV |

</details>

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_MODEL_NAME,access_MODEL_NAME,model_MODEL_NAME,base.group_user,1,0,0,0
```
