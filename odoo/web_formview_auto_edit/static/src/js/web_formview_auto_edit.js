//-*- coding: utf-8 -*-
//############################################################################
//
//   OpenERP, Open Source Management Solution
//   This module copyright (C) 2014 Therp BV (<http://therp.nl>).
//
//   This program is free software: you can redistribute it and/or modify
//   it under the terms of the GNU Affero General Public License as
//   published by the Free Software Foundation, either version 3 of the
//   License, or (at your option) any later version.
//
//   This program is distributed in the hope that it will be useful,
//   but WITHOUT ANY WARRANTY; without even the implied warranty of
//   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//   GNU Affero General Public License for more details.
//
//   You should have received a copy of the GNU Affero General Public License
//   along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//############################################################################

openerp.web_formview_auto_edit = function(instance)
{
    instance.web.ViewManager.include({
        do_create_view: function(view_type) {
            // Lazy loading of views
            // 重写创建视图方法，增加跳转到form界面自动是编辑状态，方式：action中context设定form_open_edit=True
            var self = this;
            var view = this.views[view_type];
            var viewclass = this.registry.get_object(view_type);
            var options = _.clone(view.options);
            if (view_type === "form" && this.action && (this.action.target == 'new' || this.action.target == 'inline' || this.action.context.form_open_edit)) {
                options.initial_mode = 'edit';
            }
            var controller = new viewclass(this, this.dataset, view.view_id, options);

            controller.on('history_back', this, function() {
                var am = self.getParent();
                if (am && am.trigger) {
                    return am.trigger('history_back');
                }
            });

            controller.on("change:title", this, function() {
                if (self.active_view === view_type) {
                    self.set_title(controller.get('title'));
                }
            });

            if (view.embedded_view) {
                controller.set_embedded_view(view.embedded_view);
            }
            controller.on('switch_mode', self, this.switch_mode);
            controller.on('previous_view', self, this.prev_view);

            var container = this.$el.find("> div > div > .oe_view_manager_body > .oe_view_manager_view_" + view_type);
            var view_promise = controller.appendTo(container);
            this.views[view_type].controller = controller;
            return $.when(view_promise).done(function() {
                self.views[view_type].deferred.resolve(view_type);
                if (self.searchview
                        && self.flags.auto_search
                        && view.controller.searchable !== false) {
                    self.searchview.ready.done(self.searchview.do_search);
                } else {
                    self.view_completely_inited.resolve();
                }
                self.trigger("controller_inited",view_type,controller);
            });
        },
    });
}
