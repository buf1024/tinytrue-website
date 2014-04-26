begin;
-- settings
insert into tinylog_settings(id, title, brand, copy_info, blog_display_count,
blog_notify, blog_overview, blog_overview_count, game_menu_count)
values (1, 'the bigfalse small website', 'BIGFALSE', '<em>Copyright /&copy; 
buf1024@gmail.com, Power by<a href="http://nginx.org/" target="_blank">nginx</a>
 /&/&<a href="http://www.raspberrypi.org/" target="_blank">raspbery pi</a> /&/& 
 <a href="http://pidora.ca/" target="_blank">pidaro</a>.</em>' 10,
 1, 0, 500, 5);
 
 -- modules
 insert into tinylog_module(id, name, title, "desc", enable, display_count, setting_id)
 values(1, 'comment', '∆¿¬€¡–±Ì', 1, 5, 1)
 
 commit;
 