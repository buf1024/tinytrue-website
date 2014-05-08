begin;

-- settings
delete from tinylog_settings;
insert into tinylog_settings(id, title, brand, copy_info, blog_display_count,
blog_notify, blog_overview, game_menu_count, create_time, update_time)
values (1, 'THE BIGFALSE', 'BIGFALSE', '<em>Copyright &copy; 
2014 buf1024@gmail.com, Power by <a href="http://nginx.org/" target="_blank">nginx</a>
  && <a href="http://www.raspberrypi.org/" target="_blank">raspbery pi</a> && 
 <a href="http://pidora.ca/" target="_blank">pidaro</a>.</em>', 10,
 1, 1, 5, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
 
 -- modules
delete from tinylog_module;
insert into tinylog_module(id, name, "desc", visiable, display_count, 
    create_time, update_time)
 values(1, '最新评论', '最新评论', 1, 5, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
insert into tinylog_module(id, name, "desc", visiable, display_count, 
    create_time, update_time)
 values(2, '阅读排行', '阅读排行', 1, 5, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
 insert into tinylog_module(id, name, "desc", visiable, display_count, 
    create_time, update_time)
 values(3, '评论排行', '评论排行', 1, 5, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
 insert into tinylog_module(id, name, "desc", visiable, display_count, 
    create_time, update_time)
 values(4, '分类', '分类', 1, 5, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
insert into tinylog_module(id, name, "desc", visiable, display_count, 
    create_time, update_time)
 values(5, '标签', '标签', 1, 5, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
 insert into tinylog_module(id, name, "desc", visiable, display_count, 
    create_time, update_time)
 values(6, '归档', '归档', 1, 5, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
 
 -- admin user
 delete from tinylog_user;
 insert into tinylog_user(id, name, password, email, create_time, update_time)
 values(1, 'buf1024', '111111', 'buf1024@gmail.com', '2014-04-01 00:00:00', '2014-04-01 00:00:00');
 
 -- catalog
delete from tinylog_catalog;
insert into tinylog_catalog(id, name, "desc", "type", create_time, update_time)
values(1, '益智', '益智游戏', 2, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
insert into tinylog_catalog(id, name, "desc", "type", create_time, update_time)
values(2, '杂项', '未归类杂项', 1, '2014-04-01 00:00:00', '2014-04-01 00:00:00');
 
 -- game
 --delete from tinylog_game;
 --insert into tinylog_game(id, name, "desc", image, visiable, hot, create_time, update_time, catalog_id)
 --values(1, '2048', 'an 2048 game', '/game/2048/game.png', 1, 0, '2014-04-01 00:00:00', '2014-04-01 00:00:00', 1);
  
 commit;
 