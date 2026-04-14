# -*- coding: utf-8 -*-

from mylib import *

# doit()は、CSS、HTML、Javascript の３値を返すように定義する
def doit(title="",cookie={},param={}):
    """HTMLコンテンツ出力部を記述"""

    html = """<h4>Happy! World!</h4>"""
    
    help = """<div class="exercise">
<h4>演習問題</h4>
<p>m_hello.py の doit() 関数return文の 'Hello World!' を自由に書き換えて
http://localhost/sc/index.html をリロード(強制リロード)してみましょう。</p>

<hr />
<h4>強制リロード(ハード再読み込み)する方法</h4>
通常のリロードでは書き換わらない場合があるので、必ず<b>強制リロード</b>してみる！

<dl>
<dt>Chromeの場合</dt>
<dd>
  <ol>
  <li>リロードボタンの右クリックないし長押しでメニューが出てくる
      <div style="margin:5px 0;"><img src="images/reloadmenu.png" /></div>
  </li>
  <li>ここの「ハード再読み込み」を選択</li>
  </ol>
</dd>
<dt>Firefoxの場合</dt>
<dd>
  Chromeと同じショートカットキー(Ctrl+Shift+R)を試してみる
</dd>
</div>
"""
    
    cis_moodle = """<html dir="ltr" lang="ja" xml:lang="ja" class="yui3-js-enabled"><head>
    <title>コース: サービスコンピューティング2026 | CIS Moodle</title>
    <link rel="shortcut icon" href="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/theme/1775374816/favicon">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="keywords" content="moodle, コース: サービスコンピューティング2026 | CIS Moodle">
<link rel="stylesheet" type="text/css" href="https://cms.cis.k.hosei.ac.jp/theme/yui_combo.php?rollup/3.18.1/yui-moodlesimple-min.css"><script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://cms.cis.k.hosei.ac.jp/theme/styles.php/classic/1775374816_1775369614/all">
<script>
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/cms.cis.k.hosei.ac.jp","apibase":"https:\/\/cms.cis.k.hosei.ac.jp\/r.php\/api","homeurl":{},"sesskey":"7m7M1NdVAz","sessiontimeout":"28800","sessiontimeoutwarning":"1200","themerev":"1775374816","slasharguments":1,"theme":"classic","iconsystemmodule":"core\/icon_system_fontawesome","jsrev":"1775374816","admin":"admin","svgicons":true,"usertimezone":"\u30a2\u30b8\u30a2\/\u6771\u4eac","language":"ja","courseId":15,"courseContextId":76,"contextid":76,"contextInstanceId":15,"langrev":1775503445,"templaterev":"1775374816","siteId":1,"userId":326};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''}
if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else{me.path=component+'/'+component+'.'+me.type}};
YUI_config = {"debug":false,"base":"https:\/\/cms.cis.k.hosei.ac.jp\/lib\/yuilib\/3.18.1\/","comboBase":"https:\/\/cms.cis.k.hosei.ac.jp\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/cms.cis.k.hosei.ac.jp\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/cms.cis.k.hosei.ac.jp\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/cms.cis.k.hosei.ac.jp\/theme\/yui_combo.php?m\/1775374816\/","combine":true,"comboBase":"https:\/\/cms.cis.k.hosei.ac.jp\/theme\/yui_combo.php?","ext":false,"root":"m\/1775374816\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core_availability-form":{"requires":["base","node","event","event-delegate","panel","moodle-core-notification-dialogue","json"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-util":{"requires":["node","moodle-core-actionmenu"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form","datatype-date-format"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-qbank_editquestion-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-tool_lp-dragdrop-reorder":{"requires":["moodle-core-dragdrop"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","transition","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-alert","moodle-core-notification-warning","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]}}},"gallery":{"name":"gallery","base":"https:\/\/cms.cis.k.hosei.ac.jp\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/cms.cis.k.hosei.ac.jp\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1775374816\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/cms.cis.k.hosei.ac.jp\/lib\/javascript.php\/1775374816\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker","moodle-core-notification-dialogue"]},"core_comment":{"name":"core_comment","fullpath":"https:\/\/cms.cis.k.hosei.ac.jp\/lib\/javascript.php\/1775374816\/comment\/comment.js","requires":["base","io-base","node","json","yui2-animation","overlay","escape"]}},"logInclude":[],"logExclude":[],"logLevel":null};
M.yui.loader = {modules: {}};

//]]>
</script>

<meta name="robots" content="noindex">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="core/first" src="https://cms.cis.k.hosei.ac.jp/lib/requirejs.php/1775374816/core/first.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="jqueryprivate" src="https://cms.cis.k.hosei.ac.jp/lib/javascript.php/1775374816/lib/requirejs/jquery-private.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="jquery" src="https://cms.cis.k.hosei.ac.jp/lib/javascript.php/1775374816/lib/jquery/jquery-3.7.1.min.js"></script></head>
<body id="page-course-view-topics" class="format-topics limitedwidth  path-course path-course-view chrome dir-ltr lang-ja yui-skin-sam yui3-skin-sam cms-cis-k-hosei-ac-jp pagelayout-course course-15 context-76 category-7 theme  jsenabled">

<div id="page-wrapper" class="d-print-block">

    <div>
    <a class="visually-hidden-focusable" href="#maincontent">メインコンテンツへスキップする</a>
</div><script src="https://cms.cis.k.hosei.ac.jp/lib/javascript.php/1775374816/lib/polyfills/polyfill.js"></script>
<script src="https://cms.cis.k.hosei.ac.jp/theme/yui_combo.php?rollup/3.18.1/yui-moodlesimple-min.js"></script><script src="https://cms.cis.k.hosei.ac.jp/lib/javascript.php/1775374816/lib/javascript-static.js"></script>
<script>
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>



    <nav class="fixed-top navbar navbar-bootswatch navbar-expand moodle-has-zindex">
        <div class="container-fluid">
            <a href="https://cms.cis.k.hosei.ac.jp/my/" class="navbar-brand d-flex align-items-center m-1 p-0 aabtn">
                    <span class="sitename">CIS Moodle</span>
            </a>
    
            <ul class="navbar-nav d-none d-md-flex">
                <!-- custom_menu -->
                <li class="dropdown nav-item">
    <a class="dropdown-toggle nav-link" id="drop-down-69d45b23ec19a69d45b23c726e31" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" href="#" title="言語設定" aria-controls="drop-down-menu-69d45b23ec19a69d45b23c726e31">
        日本語 &lrm;(ja)&lrm;
    </a>
    <div class="dropdown-menu" role="menu" id="drop-down-menu-69d45b23ec19a69d45b23c726e31" aria-labelledby="drop-down-69d45b23ec19a69d45b23c726e31">
                <a class="dropdown-item" role="menuitem" href="https://cms.cis.k.hosei.ac.jp/course/view.php?id=15&amp;lang=en" lang="en">English &lrm;(en)&lrm;</a>
                <a class="dropdown-item" role="menuitem" href="https://cms.cis.k.hosei.ac.jp/course/view.php?id=15&amp;lang=ja">日本語 &lrm;(ja)&lrm;</a>
    </div>
</li>
                <!-- page_heading_menu -->
                
            </ul>
            <div id="usernavigation" class="navbar-nav my-1 ms-auto">
                <div class="divider border-start h-50 align-self-center mx-1"></div>
                
                <div class="popover-region collapsed popover-region-notifications" id="nav-notification-popover-container" data-userid="326" data-region="popover-region">
    <div class="popover-region-toggle nav-link icon-no-margin" data-region="popover-region-toggle" aria-controls="popover-region-container-69d45b23ed25669d45b23c726e32" aria-haspopup="true" aria-expanded="false" aria-label=" 新しい通知がない通知ウィンドウを表示する   " title=" 新しい通知がない通知ウィンドウを表示する   " tabindex="0" role="button">
                <i class="icon fa fa-bell fa-fw " aria-hidden="true"></i>
        <div class="count-container hidden" data-region="count-container" aria-hidden="true">
            0
        </div>

    </div>
    <div aria-modal="true" tabindex="-1" id="popover-region-container-69d45b23ed25669d45b23c726e32" class="popover-region-container" data-region="popover-region-container" aria-hidden="true" aria-label="通知ウィンドウ" role="dialog">
        <div class="popover-region-header-container">
            <h3 class="popover-region-header-text" data-region="popover-region-header-text">通知</h3>
            <div class="popover-region-header-actions" data-region="popover-region-header-actions">        <a class="mark-all-read-button btn btn-sm btn-link m-0 py-0 icon-no-margin" href="#" title="すべてを既読にする" data-action="mark-all-read" role="button" aria-label="すべてを既読にする">
            <span class="normal-icon"><i class="icon fa fa-check fa-fw " aria-hidden="true"></i></span>
            <span class="loading-icon icon-no-margin"><i class="icon fa fa-spinner fa-spin fa-fw " title="読み込み中" role="img" aria-label="読み込み中"></i></span>
            <span aria-live="polite" class="visually-hidden" data-region="notification-read-feedback"></span>
        </a>
            <a href="https://cms.cis.k.hosei.ac.jp/message/notificationpreferences.php" title="通知プレファレンス" aria-label="通知プレファレンス" class="btn btn-sm btn-link m-0 py-0 icon-no-margin">
                <i class="icon fa fa-gear fa-fw " aria-hidden="true"></i></a>
        <button type="button" class="btn btn-sm btn-link m-0 py-0 icon-no-margin" aria-label="閉じる" title="閉じる" data-action="close-notification-popover">
            <i class="icon fa fa-xmark fa-fw " aria-hidden="true"></i>
        </button>
</div>
        </div>
        <div class="popover-region-content-container" data-region="popover-region-content-container">
            <div class="popover-region-content" data-region="popover-region-content">
                        <div class="all-notifications" data-region="all-notifications" role="log" aria-busy="false" aria-atomic="false" aria-relevant="additions"></div>
        <div class="empty-message" tabindex="0" data-region="empty-message">あなたに通知はありません。</div>

            </div>
            <span class="loading-icon icon-no-margin"><i class="icon fa fa-spinner fa-spin fa-fw " title="読み込み中" role="img" aria-label="読み込み中"></i></span>
        </div>
                <a class="see-all-link" href="https://cms.cis.k.hosei.ac.jp/message/output/popup/notifications.php">
                    <div class="popover-region-footer-container">
                        <div class="popover-region-seeall-text">すべてを表示する</div>
                    </div>
                </a>
    </div>
</div>
                <div class="d-flex align-items-stretch usermenu-container" data-region="usermenu">
                    <div class="usermenu"><div class="action-menu moodle-actionmenu nowrap-items" id="action-menu-0" data-enhance="moodle-core-actionmenu">

        <div class="menubar d-flex " id="action-menu-0-menubar">

            


                <div class="action-menu-trigger">
                    <div class="dropdown">
                        <a href="#" tabindex="0" class="nav-link dropdown-toggle icon-no-margin" id="action-menu-toggle-0" aria-label="ユーザメニュー" data-bs-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false" aria-controls="action-menu-0-menu">
                            
                            <span class="userbutton"><span class="usertext me-1">霍 永豪</span><span class="avatars"><span class="avatar current"><span class="userinitials size-35" title="霍 永豪" aria-label="霍 永豪" role="img">霍永</span></span></span></span>
                                
                            <b class="caret"></b>
                        </a>
                            <div class="dropdown-menu menu dropdown-menu-end" id="action-menu-0-menu" data-rel="menu-content" aria-labelledby="action-menu-toggle-0" role="menu">
                                                                <a href="https://cms.cis.k.hosei.ac.jp/user/profile.php" class="dropdown-item menu-action" role="menuitem" data-title="profile,moodle" tabindex="-1">
                                <span class="menu-action-text">プロファイル</span>
                        </a>
                    <div class="dropdown-divider" role="presentation"><span class="filler">&nbsp;</span></div>
                                                                <a href="https://cms.cis.k.hosei.ac.jp/grade/report/overview/index.php" class="dropdown-item menu-action" role="menuitem" data-title="grades,grades" tabindex="-1">
                                <span class="menu-action-text">評定</span>
                        </a>
                                                                <a href="https://cms.cis.k.hosei.ac.jp/calendar/view.php?view=month" class="dropdown-item menu-action" role="menuitem" data-title="calendar,core_calendar" tabindex="-1">
                                <span class="menu-action-text">カレンダー</span>
                        </a>
                                                                <a href="https://cms.cis.k.hosei.ac.jp/user/files.php" class="dropdown-item menu-action" role="menuitem" data-title="privatefiles,moodle" tabindex="-1">
                                <span class="menu-action-text">プライベートファイル</span>
                        </a>
                                                                <a href="https://cms.cis.k.hosei.ac.jp/reportbuilder/index.php" class="dropdown-item menu-action" role="menuitem" data-title="reports,core_reportbuilder" tabindex="-1">
                                <span class="menu-action-text">レポート</span>
                        </a>
                    <div class="dropdown-divider" role="presentation"><span class="filler">&nbsp;</span></div>
                                                                <a href="https://cms.cis.k.hosei.ac.jp/user/preferences.php" class="dropdown-item menu-action" role="menuitem" data-title="preferences,moodle" tabindex="-1">
                                <span class="menu-action-text">プレファレンス</span>
                        </a>
                    <div class="dropdown-divider" role="presentation"><span class="filler">&nbsp;</span></div>
                                                                <a href="https://cms.cis.k.hosei.ac.jp/login/logout.php?sesskey=7m7M1NdVAz" class="dropdown-item menu-action" role="menuitem" data-title="logout,moodle" tabindex="-1">
                                <span class="menu-action-text">ログアウト</span>
                        </a>
                            </div>
                    </div>
                </div>

        </div>

</div></div>
                </div>
            </div>
        </div>
    </nav>

    <div id="page" class="container-fluid d-print-block stateready">
        <header id="page-header" class="row">
    <div class="col-12 pt-3 pb-3">
        <div class="card ">
            <div class="card-body ">
                <div class="d-flex align-items-center">
                    <div class="me-auto">
                    <div class="page-context-header d-flex flex-wrap align-items-center mb-2">
    <div class="page-header-headings">
        <h1 class="h2 mb-0">サービスコンピューティング2026</h1>
    </div>
</div>
                    </div>
                    <div class="header-actions-container flex-shrink-0" data-region="header-actions-container">
                    </div>
                </div>
                <div class="d-flex flex-wrap">
                    <div id="page-navbar">
                        <nav aria-label="ブレッドクラム">
    <ol class="breadcrumb">
                <li class="breadcrumb-item">
                    <a href="https://cms.cis.k.hosei.ac.jp/my/">
                        ダッシュボード
                    </a>
                </li>
        
                <li class="breadcrumb-item">
                    <a href="https://cms.cis.k.hosei.ac.jp/my/courses.php">
                        マイコース
                    </a>
                </li>
        
                <li class="breadcrumb-item">
                    <a href="https://cms.cis.k.hosei.ac.jp/course/index.php?categoryid=1">
                        2026年度
                    </a>
                </li>
        
                <li class="breadcrumb-item">
                    <a href="https://cms.cis.k.hosei.ac.jp/course/index.php?categoryid=7">
                        2026年度 - 3年生春学期
                    </a>
                </li>
        
                <li class="breadcrumb-item">
                    <a href="https://cms.cis.k.hosei.ac.jp/course/view.php?id=15" aria-current="page" title="サービスコンピューティング2026">
                        サービスコンピューティング2026
                    </a>
                </li>
        </ol>
</nav>
                    </div>
                    <div class="ms-auto d-flex">
                        
                    </div>
                    <div id="course-header">
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>

        <div id="page-content" class="d-flex flex-wrap  blocks-pre   blocks-post  d-print-block">
            <div id="region-main-box" class="region-main">
                <div id="region-main" class="region-main-content">
                    <span class="notifications" id="user-notifications"></span>
                    <div role="main"><span id="maincontent"></span><div class="course-content"><div id="course-format-69d45b24062b469d45b23c726e44">
    <h2 class="accesshide">セクションアウトライン</h2>
    
    <ul class="topics section-list" data-for="course_sectionlist">
                <li id="section-0" class="section course-section main  clearfix
                             
                            " data-sectionid="0" data-sectionreturnnum="" data-for="section" data-id="210" data-number="0" data-sectionname="一般" data-indexed="true">
                    <div class="section-item">
                            <div class="course-section-header d-flex" data-for="section_title" data-id="210" data-number="0">
                                            <div class="bulkselect align-self-center d-none" data-for="sectionBulkSelect">
                                                <input id="sectionCheckbox210" type="checkbox" data-id="210" data-action="toggleSelectionSection" data-bulkcheckbox="1">
                                                <label class="visually-hidden" for="sectionCheckbox210">
                                                     セクション 一般 を選択する 
                                                </label>
                                            </div>
                                                    <div class="d-flex align-items-center position-relative">
                                                        <a role="button" data-bs-toggle="collapse" data-for="sectiontoggler" href="#coursecontentcollapseid210" id="collapsesectionid210" aria-expanded="true" aria-controls="coursecontentcollapseid210" class="btn btn-icon me-3 icons-collapse-expand
                                                                " aria-label="一般">
                                                        <span class="expanded-icon icon-no-margin p-2" title="折りたたむ">
                                                            <i class="icon fa fa-chevron-down fa-fw " aria-hidden="true"></i>
                                                            <span class="visually-hidden">折りたたむ</span>
                                                        </span>
                                                        <span class="collapsed-icon icon-no-margin p-2" title="展開する">
                                                            <span class="dir-rtl-hide"><i class="icon fa fa-chevron-right fa-fw " aria-hidden="true"></i></span>
                                                            <span class="dir-ltr-hide"><i class="icon fa fa-chevron-left fa-fw " aria-hidden="true"></i></span>
                                                            <span class="visually-hidden">展開する</span>
                                                        </span>
                                                        </a>
                                                        <h3 class="h4 sectionname course-content-item d-flex align-self-stretch align-items-center mb-0" id="sectionid-210-title" data-for="section_title" data-id="210" data-number="0">
                                                            <a href="https://cms.cis.k.hosei.ac.jp/course/section.php?id=210">一般</a>
                                                        </h3>
                                                    </div>
                                <div data-region="sectionbadges" class="sectionbadges d-flex align-items-center">
                                </div>
                                        <div class="flex-fill d-flex justify-content-end me-2 align-self-start mt-2">
                                            <a id="collapsesections" class="section-collapsemenu" href="#" aria-expanded="true" role="button" data-toggle="toggleall" aria-controls="collapsesectionid210 collapsesectionid211">
                                                <span class="collapseall text-nowrap">すべてを折りたたむ</span>
                                                <span class="expandall text-nowrap">すべてを展開する</span>
                                            </a>
                                        </div>
                            </div>
                            <div id="coursecontentcollapseid210" class="content course-content-item-content collapse show">
                                <div class=" my-3" data-for="sectioninfo">
                                                <div class="summarytext">
                                                    <div class="no-overflow"><p>2026年度春学期のサービスコンピューティングの講義サイトです。</p>
<p><span style="font-size: 0.9375rem;">各種問合せは、</span></p>
<ul>
<li><span style="font-size: 0.9375rem;">準備中: メーリングリスト j0543support@ml.cis.k.hosei.ac.jp …&nbsp;</span>講義連絡用（教員・TA）</li>
</ul>
<ul>
<li><span style="font-size: 0.9375rem;"><a class="autolink" title="トラブルシューティング・質問コーナー" href="https://cms.cis.k.hosei.ac.jp/mod/forum/view.php?id=283">トラブルシューティング・質問コーナー</a>（Moodle内）… 開講後</span></li>
</ul>
<p></p>
<p><span style="font-size: 0.9375rem;">&nbsp;にてお願いします。<br></span></p>
<p></p>
<p></p>
<p></p></div>
                                                </div>
                                            <div class="section_availability">
                                            </div>
                                </div>
                                        <ul class="section m-0 p-0 img-text  d-block " data-for="cmlist">
                                                    <li class="activity forum modtype_forum  hasinfo " id="module-15" data-for="cmitem" data-id="15" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="アナウンスメント" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox15" type="checkbox" data-id="15" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox15">
                                                                                活動 アナウンスメント を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller collaboration  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/forum/1775374816/monologo?filtericon=1" class="activityicon " data-region="activity-icon" data-id="15" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_forum position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/forum/view.php?id=15" class=" aalink stretched-link" onclick="">        <span class="instancename">アナウンスメント <span class="accesshide "> フォーラム</span></span>    </a>
                                                                                                            
                                                                                                            <span class="ms-1">
                                                                                                                <span class="activitybadge badge rounded-pill ">
                                                                                                                        
                                                                                                                </span>
                                                                                                            </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                                    <li class="activity forum modtype_forum  hasinfo " id="module-283" data-for="cmitem" data-id="283" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="トラブルシューティング・質問コーナー" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox283" type="checkbox" data-id="283" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox283">
                                                                                活動 トラブルシューティング・質問コーナー を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller collaboration  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/forum/1775374816/monologo?filtericon=1" class="activityicon " data-region="activity-icon" data-id="283" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_forum position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/forum/view.php?id=283" class=" aalink stretched-link" onclick="">        <span class="instancename">トラブルシューティング・質問コーナー <span class="accesshide "> フォーラム</span></span>    </a>
                                                                                                            
                                                                                                            <span class="ms-1">
                                                                                                                <span class="activitybadge badge rounded-pill ">
                                                                                                                        
                                                                                                                </span>
                                                                                                            </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                            <div class="activity-altcontent text-break activity-description">
                                                                                <div class="no-overflow"><div class="no-overflow"><p></p>
<p><strong><strong>講義内容に関する質疑等に使ってください（回答者は教員・TAに限らず、皆さんの参加を歓迎します）</strong></strong></p>
<p></p>
<ul>
<li>講義に関係のない話題は投稿しないこと</li>
<li>他の人にも共通的で有用な質疑を歓迎します</li>
</ul>
<p><strong>環境・演習等におけるトラブルシューティングのために使ってください。</strong></p>
<p></p>
<ul>
<li>XAMPP環境構築、演習用Webサイトに関する話題を投稿すること</li>
<li>問題を明確にする、自己解決に努める、それでもうまくいかない場合、友人に聞いてみる、友人とともに解決する</li>
<li>最終的にうまくいった場合、その問題と解決策をここに上げる</li>
<li>それでも解決しない場合、ここで皆と問題を共有する、解を持つ人は解決策をここに上げる</li>
</ul>
<p><strong>トラブルシューティング際に、</strong><strong>解決の早道となる記載すべき事項は以下になります。</strong></p>
<ul>
<li>添付ファイルは100KB×４つまで可能にしました。有効に使ってください。</li>
<li>インストールガイド等に沿って進めてもらっていると思いますが、どのステップまでうまくいってどこで躓いたのかを明確に示してください。</li>
<li>ガイドのなかには留意事項等も記載していますが、それらをすべて確認し、クリアしているかも示してください。</li>
<li>不具合の状況を示すには、画面のキャプチャが有効です。</li>
<li>ソースコードの修正等が影響していると思われる場合は、どの行をどう直したのか、を抜き出して示してください。ソース全体を添付するのは最終手段になります。</li>
</ul>
<p></p>
<p></p></div></div>
                                                                            </div>
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                                    <li class="activity resource modtype_resource  hasinfo " id="module-284" data-for="cmitem" data-id="284" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="XAMPP環境・演習用Webサイト構築ガイド" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox284" type="checkbox" data-id="284" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox284">
                                                                                活動 XAMPP環境・演習用Webサイト構築ガイド を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller content  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/core/1775374816/f/pdf?filtericon=1" class="activityicon " data-region="activity-icon" data-id="284" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_resource position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/resource/view.php?id=284" class=" aalink stretched-link" onclick="">        <span class="instancename">XAMPP環境・演習用Webサイト構築ガイド <span class="accesshide "> ファイル</span></span>    </a>
                                                                                                            
                                                                                                            <span class="ms-1">
                                                                                                                <span class="activitybadge badge rounded-pill ">
                                                                                                                        
                                                                                                                </span>
                                                                                                            </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                                <div class="activity-completion align-self-start ms-sm-2">
                                                                                        <div data-region="activity-information" data-activityname="XAMPP環境・演習用Webサイト構築ガイド" class="activity-information">
                                                                                            <div data-region="completion-info">
                                                                                            
                                                                                                                        <button class="btn btn-subtle-body  btn-sm text-nowrap" data-action="toggle-manual-completion" data-toggletype="manual:mark-done" data-cmid="284" data-activityname="XAMPP環境・演習用Webサイト構築ガイド" data-withavailability="0" title="XAMPP環境・演習用Webサイト構築ガイド を完了マークする" aria-label="XAMPP環境・演習用Webサイト構築ガイド を完了マークする">
                                                                                                                            完了マークする
                                                                                                                        </button>
                                                                                                                
                                                                                            </div>
                                                                                        </div>
                                                                                </div>
                                                                    
                                                                    
                                                                            <div class="activity-altcontent text-break activity-description">
                                                                                <div class="no-overflow"><div class="no-overflow"><p>本講義の演習で使用するブラウザのインストール、XAMPP環境構築、XAMPP環境で演習用WebサイトおよびPython3を使えるようにするガイドです。</p>
<p></p>
<ul>
<li><strong>4/16の講義までに各自準備しておくこと</strong></li>
<li>問題を明確にする、自己解決に努める、それでもうまくいかない場合、友人に聞いてみる、友人とともに解決する</li>
<li>「サービスコンピューティング トラブルシューティング」フォーラムを活用する</li>
</ul>
<p></p></div></div>
                                                                            </div>
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                                    <li class="activity resource modtype_resource  hasinfo " id="module-285" data-for="cmitem" data-id="285" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="Webサイト構築ソースコード一式" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox285" type="checkbox" data-id="285" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox285">
                                                                                活動 Webサイト構築ソースコード一式 を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller content  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/core/1775374816/f/archive?filtericon=1" class="activityicon " data-region="activity-icon" data-id="285" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_resource position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/resource/view.php?id=285" class=" aalink stretched-link" onclick="">        <span class="instancename">Webサイト構築ソースコード一式 <span class="accesshide "> ファイル</span></span>    </a>
                                                                                                            
                                                                                                            <span class="ms-1">
                                                                                                                <span class="activitybadge badge rounded-pill ">
                                                                                                                        
                                                                                                                </span>
                                                                                                            </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                                <div class="activity-completion align-self-start ms-sm-2">
                                                                                        <div data-region="activity-information" data-activityname="Webサイト構築ソースコード一式" class="activity-information">
                                                                                            <div data-region="completion-info">
                                                                                            
                                                                                                                        <button class="btn btn-subtle-body  btn-sm text-nowrap" data-action="toggle-manual-completion" data-toggletype="manual:mark-done" data-cmid="285" data-activityname="Webサイト構築ソースコード一式" data-withavailability="0" title="Webサイト構築ソースコード一式 を完了マークする" aria-label="Webサイト構築ソースコード一式 を完了マークする">
                                                                                                                            完了マークする
                                                                                                                        </button>
                                                                                                                
                                                                                            </div>
                                                                                        </div>
                                                                                </div>
                                                                    
                                                                    
                                                                            <div class="activity-altcontent text-break activity-description">
                                                                                <div class="no-overflow"><div class="no-overflow"><p>本講義の演習で使用するWebサイトのソースコード一式です。</p>
<p></p>
<ul>
<li><strong>4/16の講義までに各自準備しておくこと</strong></li>
<li>問題を明確にする、自己解決に努める、それでもうまくいかない場合、友人に聞いてみる、友人とともに解決する</li>
<li>「サービスコンピューティング トラブルシューティング」フォーラムを活用する</li>
</ul></div></div>
                                                                            </div>
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                                    <li class="activity resource modtype_resource  hasinfo " id="module-286" data-for="cmitem" data-id="286" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="演習用Webサイトのデバッグの仕方" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox286" type="checkbox" data-id="286" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox286">
                                                                                活動 演習用Webサイトのデバッグの仕方 を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller content  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/core/1775374816/f/pdf?filtericon=1" class="activityicon " data-region="activity-icon" data-id="286" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_resource position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/resource/view.php?id=286" class=" aalink stretched-link" onclick="">        <span class="instancename">演習用Webサイトのデバッグの仕方 <span class="accesshide "> ファイル</span></span>    </a>
                                                                                                            
                                                                                                            <span class="ms-1">
                                                                                                                <span class="activitybadge badge rounded-pill ">
                                                                                                                        
                                                                                                                </span>
                                                                                                            </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                                <div class="activity-completion align-self-start ms-sm-2">
                                                                                        <div data-region="activity-information" data-activityname="演習用Webサイトのデバッグの仕方" class="activity-information">
                                                                                            <div data-region="completion-info">
                                                                                            
                                                                                                                        <button class="btn btn-subtle-body  btn-sm text-nowrap" data-action="toggle-manual-completion" data-toggletype="manual:mark-done" data-cmid="286" data-activityname="演習用Webサイトのデバッグの仕方" data-withavailability="0" title="演習用Webサイトのデバッグの仕方 を完了マークする" aria-label="演習用Webサイトのデバッグの仕方 を完了マークする">
                                                                                                                            完了マークする
                                                                                                                        </button>
                                                                                                                
                                                                                            </div>
                                                                                        </div>
                                                                                </div>
                                                                    
                                                                    
                                                                            <div class="activity-altcontent text-break activity-description">
                                                                                <div class="no-overflow"><div class="no-overflow"><p>本講義の演習で使用するWebサイトで、ソースコードを書き換えを行った場合の、デバッグ支援の方法を記したものです。うまくいかない場合に試してみてください。</p>
<p></p></div></div>
                                                                            </div>
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                                    <li class="activity resource modtype_resource  hasinfo " id="module-287" data-for="cmitem" data-id="287" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="MySQL環境設定ガイド" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox287" type="checkbox" data-id="287" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox287">
                                                                                活動 MySQL環境設定ガイド を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller content  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/core/1775374816/f/pdf?filtericon=1" class="activityicon " data-region="activity-icon" data-id="287" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_resource position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/resource/view.php?id=287" class=" aalink stretched-link" onclick="">        <span class="instancename">MySQL環境設定ガイド <span class="accesshide "> ファイル</span></span>    </a>
                                                                                                            
                                                                                                            <span class="ms-1">
                                                                                                                <span class="activitybadge badge rounded-pill ">
                                                                                                                        
                                                                                                                </span>
                                                                                                            </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                                <div class="activity-completion align-self-start ms-sm-2">
                                                                                        <div data-region="activity-information" data-activityname="MySQL環境設定ガイド" class="activity-information">
                                                                                            <div data-region="completion-info">
                                                                                            
                                                                                                                        <button class="btn btn-subtle-body  btn-sm text-nowrap" data-action="toggle-manual-completion" data-toggletype="manual:mark-done" data-cmid="287" data-activityname="MySQL環境設定ガイド" data-withavailability="0" title="MySQL環境設定ガイド を完了マークする" aria-label="MySQL環境設定ガイド を完了マークする">
                                                                                                                            完了マークする
                                                                                                                        </button>
                                                                                                                
                                                                                            </div>
                                                                                        </div>
                                                                                </div>
                                                                    
                                                                    
                                                                            <div class="activity-altcontent text-break activity-description">
                                                                                <div class="no-overflow"><div class="no-overflow"><p>本講義の演習で使用するMySQLのデータベースの初期化とPython3から使えるようにするための構築ガイドです。</p>
<ul>
<li>MySQLはXAMPPのいちコンポーネントであり、XAMPPのインストールに成功していれば問題なく起動できるはずだが、もし失敗するようなら、既にそのPC上でMySQLが動作している場合</li>
<li>MySQLを起動した状態で、XAMPPコントロールからMySQLのAdminツールであるphpMyAdminを起動し、ブラウザから使用することができる</li>
<li>
<div>設定に使用するSQLは、<strong>WS-0-site.zip に同梱されている student.sql </strong>を使用</div>
</li>
<li>このデータベースの環境設定は、phpMyAdminを使用して、<strong>5/x </strong><strong>の講義日までに準備しておくこと</strong></li>
<li>「サービスコンピューティング トラブルシューティング」フォーラムを活用する</li>
</ul></div></div>
                                                                            </div>
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                                    <li class="activity assign modtype_assign  hasinfo " id="module-288" data-for="cmitem" data-id="288" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="レポート課題アップロード(6/25締切)" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox288" type="checkbox" data-id="288" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox288">
                                                                                活動 レポート課題アップロード(6/25締切) を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller assessment  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/assign/1775374816/monologo?filtericon=1" class="activityicon " data-region="activity-icon" data-id="288" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_assign position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/assign/view.php?id=288" class=" aalink stretched-link" onclick="">        <span class="instancename">レポート課題アップロード(6/25締切) </span>    </a>
                                                                                                            
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                                <div data-region="activity-dates" class="activity-dates me-sm-2">
                                                                                            <div>
                                                                                                <strong>開始:</strong> 2025年 06月 17日(火曜日) 00:00
                                                                                            </div>
                                                                                            <div>
                                                                                                <strong>期限:</strong> 2025年 06月 25日(水曜日) 23:59
                                                                                            </div>
                                                                                </div>
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                            <div class="activity-altcontent text-break activity-description">
                                                                                <div class="no-overflow"><div class="no-overflow"><p><strong>レ<span style="font-size: 0.9375rem; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';">ポート課題をアップロードしてください。</span></strong></p>
<p></p>
<ul>
<li>レポート課題の内容については、<strong>第7回講義PDFの末尾に記載</strong>しているので、これを参照すること</li>
<li>アップロードの更新は最大３回まで</li>
<li>アップロードの最終提出期限は 2024/6/26 23:59:59 まで</li>
<li>レポートは<strong style="font-size: 0.9375rem;">PDFで提出すること</strong></li>
</ul>
<p></p></div></div>
                                                                            </div>
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                                    <li class="activity forum modtype_forum  hasinfo " id="module-289" data-for="cmitem" data-id="289" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="お試しフォーラム" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox289" type="checkbox" data-id="289" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox289">
                                                                                活動 お試しフォーラム を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller collaboration  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/forum/1775374816/monologo?filtericon=1" class="activityicon " data-region="activity-icon" data-id="289" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_forum position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/forum/view.php?id=289" class=" aalink stretched-link" onclick="">        <span class="instancename">お試しフォーラム </span>    </a>
                                                                                                            
                                                                                                            <span class="ms-1">
                                                                                                                <span class="activitybadge badge rounded-pill ">
                                                                                                                        
                                                                                                                </span>
                                                                                                            </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                            </ul>
                                
                            </div>
                    </div>
                
                </li>
                <li id="section-1" class="section course-section main  clearfix
                             
                            " data-sectionid="1" data-sectionreturnnum="" data-for="section" data-id="211" data-number="1" data-sectionname="第１回" data-indexed="true">
                    <div class="section-item">
                            <div class="course-section-header d-flex" data-for="section_title" data-id="211" data-number="1">
                                            <div class="bulkselect align-self-center d-none" data-for="sectionBulkSelect">
                                                <input id="sectionCheckbox211" type="checkbox" data-id="211" data-action="toggleSelectionSection" data-bulkcheckbox="1">
                                                <label class="visually-hidden" for="sectionCheckbox211">
                                                     セクション 第１回 を選択する 
                                                </label>
                                            </div>
                                                    <div class="d-flex align-items-center position-relative">
                                                        <a role="button" data-bs-toggle="collapse" data-for="sectiontoggler" href="#coursecontentcollapseid211" id="collapsesectionid211" aria-expanded="true" aria-controls="coursecontentcollapseid211" class="btn btn-icon me-3 icons-collapse-expand
                                                                " aria-label="第１回">
                                                        <span class="expanded-icon icon-no-margin p-2" title="折りたたむ">
                                                            <i class="icon fa fa-chevron-down fa-fw " aria-hidden="true"></i>
                                                            <span class="visually-hidden">折りたたむ</span>
                                                        </span>
                                                        <span class="collapsed-icon icon-no-margin p-2" title="展開する">
                                                            <span class="dir-rtl-hide"><i class="icon fa fa-chevron-right fa-fw " aria-hidden="true"></i></span>
                                                            <span class="dir-ltr-hide"><i class="icon fa fa-chevron-left fa-fw " aria-hidden="true"></i></span>
                                                            <span class="visually-hidden">展開する</span>
                                                        </span>
                                                        </a>
                                                        <h3 class="h4 sectionname course-content-item d-flex align-self-stretch align-items-center mb-0" id="sectionid-211-title" data-for="section_title" data-id="211" data-number="1">
                                                            <a href="https://cms.cis.k.hosei.ac.jp/course/section.php?id=211">第１回</a>
                                                        </h3>
                                                    </div>
                                <div data-region="sectionbadges" class="sectionbadges d-flex align-items-center">
                                </div>
                            </div>
                            <div id="coursecontentcollapseid211" class="content course-content-item-content collapse show">
                                <div class=" my-3" data-for="sectioninfo">
                                            <div class="section_availability">
                                            </div>
                                </div>
                                        <ul class="section m-0 p-0 img-text  d-block " data-for="cmlist">
                                                    <li class="activity resource modtype_resource  hasinfo " id="module-290" data-for="cmitem" data-id="290" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="教材" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox290" type="checkbox" data-id="290" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox290">
                                                                                活動 教材 を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller content  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/core/1775374816/f/pdf?filtericon=1" class="activityicon " data-region="activity-icon" data-id="290" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_resource position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/resource/view.php?id=290" class=" aalink stretched-link" onclick="">        <span class="instancename">教材 <span class="accesshide "> ファイル</span></span>    </a>
                                                                                                            
                                                                                                            <span class="ms-1">
                                                                                                                <span class="activitybadge badge rounded-pill ">
                                                                                                                        
                                                                                                                </span>
                                                                                                            </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                                <div class="activity-completion align-self-start ms-sm-2">
                                                                                        <div data-region="activity-information" data-activityname="教材" class="activity-information">
                                                                                            <div data-region="completion-info">
                                                                                            
                                                                                                                        <button class="btn btn-subtle-body  btn-sm text-nowrap" data-action="toggle-manual-completion" data-toggletype="manual:mark-done" data-cmid="290" data-activityname="教材" data-withavailability="0" title="教材 を完了マークする" aria-label="教材 を完了マークする">
                                                                                                                            完了マークする
                                                                                                                        </button>
                                                                                                                
                                                                                            </div>
                                                                                        </div>
                                                                                </div>
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                                    <li class="activity quiz modtype_quiz  hasinfo " id="module-291" data-for="cmitem" data-id="291" data-indexed="true">
                                                            <div class="activity-item focus-control " data-activityname="コース初回アンケート" data-region="activity-card">
                                                                        <div class="bulkselect d-none" data-for="cmBulkSelect">
                                                                            <input id="cmCheckbox291" type="checkbox" data-id="291" data-action="toggleSelectionCm" data-bulkcheckbox="1" disabled="">
                                                                            <label class="visually-hidden" for="cmCheckbox291">
                                                                                活動 コース初回アンケート を選択する
                                                                            </label>
                                                                        </div>

                                                                    <div class="activity-grid ">
                                                                    
                                                                                                <div class="activity-icon activityiconcontainer smaller assessment  courseicon align-self-start me-2">
                                                                                                    <img src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/quiz/1775374816/monologo?filtericon=1" class="activityicon " data-region="activity-icon" data-id="291" alt="">
                                                                                                </div>
                                                                                    
                                                                                        <div class="activity-name-area activity-instance d-flex flex-column me-2">
                                                                                            <div class="activitytitle  modtype_quiz position-relative align-self-start">
                                                                                                <div class="activityname">
                                                                                                                <a href="https://cms.cis.k.hosei.ac.jp/mod/quiz/view.php?id=291" class=" aalink stretched-link" onclick="">        <span class="instancename">コース初回アンケート <span class="accesshide "> 小テスト</span></span>    </a>
                                                                                                            
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    
                                                                    
                                                                                <div data-region="activity-dates" class="activity-dates me-sm-2">
                                                                                            <div>
                                                                                                <strong>開始予定:</strong> 2026年 04月 8日(水曜日) 11:00
                                                                                            </div>
                                                                                            <div>
                                                                                                <strong>終了予定:</strong> 2026年 04月 15日(水曜日) 23:59
                                                                                            </div>
                                                                                </div>
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                            <div class="activity-altcontent text-break activity-description">
                                                                                <div class="no-overflow"><div class="no-overflow"><p dir="ltr" style="text-align: left;"><strong style="font-weight: bold;">未記入の人は、</strong><strong>4/8(水)～4/15(水</strong><strong>)</strong><strong>の間に必ず回答しておいてください。</strong></p></div></div>
                                                                            </div>
                                                                    
                                                                    
                                                                    </div>
                                                            </div>
                                                    </li>
                                            </ul>
                                
                            </div>
                    </div>
                
                </li>
    </ul>
</div></div></div>
                    
                    
                </div>
            </div>
            <div class="columnleft blockcolumn  has-blocks ">
                <div data-region="blocks-column" class="d-print-none">
                    <aside id="block-region-side-pre" class="block-region" data-blockregion="side-pre" data-droptarget="1" aria-labelledby="side-pre-block-region-heading"><h2 class="visually-hidden" id="side-pre-block-region-heading">ブロック</h2><a href="#sb-1" class="visually-hidden-focusable">ナビゲーション をスキップする</a>

<section id="inst9" class=" block_navigation block  card mb-3" role="navigation" data-block="navigation" data-instance-id="9" aria-labelledby="instance-9-header">

    <div class="card-body p-3">

            <h3 id="instance-9-header" class="h5 card-title d-inline">ナビゲーション</h3>


        <div class="card-text content mt-3">
            <ul class="block_tree list" role="tree" data-ajax-loader="block_navigation/nav_loader"><li class="type_unknown depth_1 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random69d45b23c726e2_group" data-collapsible="false" aria-labelledby="random69d45b23c726e1_label_1_1" tabindex="0" aria-selected="true"><p class="tree_item branch canexpand navigation_node" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e1_label_1_1" href="https://cms.cis.k.hosei.ac.jp/my/">ダッシュボード</a></p><ul id="random69d45b23c726e2_group" role="group" tabindex="-1"><li class="type_setting depth_2 item_with_icon" role="treeitem" aria-labelledby="random69d45b23c726e3_label_2_2" tabindex="-1" aria-selected="false"><p class="tree_item hasicon" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e3_label_2_2" href="https://cms.cis.k.hosei.ac.jp/?redirect=0"><i class="icon fa fa-house fa-fw navicon" aria-hidden="true" tabindex="-1"></i><span class="item-content-wrap" tabindex="-1">サイトホーム</span></a></p></li><li class="type_course depth_2 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random69d45b23c726e5_group" aria-labelledby="random69d45b23c726e3_label_2_3" tabindex="-1" aria-selected="false"><p class="tree_item branch" tabindex="-1"><span tabindex="-1" id="random69d45b23c726e3_label_2_3" title="Hosei CIS Education Support Server">サイトページ</span></p><ul id="random69d45b23c726e5_group" role="group" aria-hidden="true" tabindex="-1"><li class="type_custom depth_3 item_with_icon" role="treeitem" aria-labelledby="random69d45b23c726e6_label_3_5" tabindex="-1" aria-selected="false"><p class="tree_item hasicon" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e6_label_3_5" href="https://cms.cis.k.hosei.ac.jp/my/courses.php"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true" tabindex="-1"></i><span class="item-content-wrap" tabindex="-1">マイコース</span></a></p></li><li class="type_custom depth_3 item_with_icon" role="treeitem" aria-labelledby="random69d45b23c726e6_label_3_6" tabindex="-1" aria-selected="false"><p class="tree_item hasicon" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e6_label_3_6" href="https://cms.cis.k.hosei.ac.jp/badges/index.php?type=1"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true" tabindex="-1"></i><span class="item-content-wrap" tabindex="-1">サイトバッジ</span></a></p></li><li class="type_setting depth_3 item_with_icon" role="treeitem" aria-labelledby="random69d45b23c726e6_label_3_7" tabindex="-1" aria-selected="false"><p class="tree_item hasicon" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e6_label_3_7" href="https://cms.cis.k.hosei.ac.jp/tag/search.php"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true" tabindex="-1"></i><span class="item-content-wrap" tabindex="-1">タグ</span></a></p></li><li class="type_activity depth_3 item_with_icon" role="treeitem" aria-labelledby="random69d45b23c726e6_label_3_9" tabindex="-1" aria-selected="false"><p class="tree_item hasicon" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e6_label_3_9" title="フォーラム" href="https://cms.cis.k.hosei.ac.jp/mod/forum/view.php?id=1"><img class="icon navicon" alt="フォーラム" title="フォーラム" src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/forum/1775374816/monologo" tabindex="-1"><span class="item-content-wrap" tabindex="-1">サイトアナウンスメント</span></a></p></li></ul></li><li class="type_system depth_2 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random69d45b23c726e11_group" aria-labelledby="random69d45b23c726e3_label_2_10" tabindex="-1" aria-selected="false"><p class="tree_item branch" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e3_label_2_10" href="https://cms.cis.k.hosei.ac.jp/my/courses.php">マイコース</a></p><ul id="random69d45b23c726e11_group" role="group" tabindex="-1"><li class="type_unknown depth_3 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random69d45b23c726e13_group" aria-labelledby="random69d45b23c726e12_label_3_11" tabindex="-1" aria-selected="false"><p class="tree_item branch" tabindex="-1"><span tabindex="-1" id="random69d45b23c726e12_label_3_11">2026年度</span></p><ul id="random69d45b23c726e13_group" role="group" tabindex="-1"><li class="type_unknown depth_4 contains_branch" role="treeitem" aria-expanded="true" aria-owns="random69d45b23c726e15_group" aria-labelledby="random69d45b23c726e14_label_4_12" tabindex="-1" aria-selected="false"><p class="tree_item branch" tabindex="-1"><span tabindex="-1" id="random69d45b23c726e14_label_4_12">2026年度 - 3年生春学期</span></p><ul id="random69d45b23c726e15_group" role="group" tabindex="-1"><li class="type_course depth_5 contains_branch current_branch" role="treeitem" aria-expanded="true" aria-owns="random69d45b23c726e17_group" aria-labelledby="random69d45b23c726e16_label_5_13" tabindex="-1" aria-selected="false"><p class="tree_item branch active_tree_node canexpand" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e16_label_5_13" title="サービスコンピューティング2026" href="https://cms.cis.k.hosei.ac.jp/course/view.php?id=15">サービスコンピューティング2026</a></p><ul id="random69d45b23c726e17_group" role="group" tabindex="-1"><li class="type_container depth_6 contains_branch" role="treeitem" aria-expanded="false" aria-owns="random69d45b23c726e19_group" aria-labelledby="random69d45b23c726e18_label_6_14" tabindex="-1" aria-selected="false"><p class="tree_item branch" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e18_label_6_14" href="https://cms.cis.k.hosei.ac.jp/user/index.php?id=15">参加者</a></p><ul id="random69d45b23c726e19_group" role="group" aria-hidden="true" tabindex="-1"><li class="type_user depth_7 item_with_icon" role="treeitem" aria-labelledby="random69d45b23c726e20_label_7_15" tabindex="-1" aria-selected="false"><p class="tree_item hasicon" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e20_label_7_15" href="https://cms.cis.k.hosei.ac.jp/user/view.php?id=326&amp;course=15"><i class="icon fa fa-square fa-fw navicon" aria-hidden="true" tabindex="-1"></i><span class="item-content-wrap" tabindex="-1">霍 永豪</span></a></p></li></ul></li><li class="type_setting depth_6 item_with_icon" role="treeitem" aria-labelledby="random69d45b23c726e18_label_6_16" tabindex="-1" aria-selected="false"><p class="tree_item hasicon" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e18_label_6_16" href="https://cms.cis.k.hosei.ac.jp/admin/tool/lp/coursecompetencies.php?courseid=15"><i class="icon fa fa-list-check fa-fw navicon" aria-hidden="true" tabindex="-1"></i><span class="item-content-wrap" tabindex="-1">コンピテンシ</span></a></p></li><li class="type_container depth_6 item_with_icon" role="treeitem" aria-labelledby="random69d45b23c726e18_label_6_17" tabindex="-1" aria-selected="false"><p class="tree_item hasicon" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e18_label_6_17" href="https://cms.cis.k.hosei.ac.jp/course/overview.php?id=15"><i class="icon fa fa-info fa-fw navicon" aria-hidden="true" tabindex="-1"></i><span class="item-content-wrap" tabindex="-1">活動</span></a></p></li><li class="type_structure depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_210" data-node-key="210" data-node-type="30" aria-labelledby="random69d45b23c726e18_label_6_18" tabindex="-1" aria-selected="false"><p class="tree_item branch" id="expandable_branch_30_210" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e18_label_6_18" href="https://cms.cis.k.hosei.ac.jp/course/section.php?id=210">一般</a></p></li><li class="type_structure depth_6 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_30_211" data-node-key="211" data-node-type="30" aria-labelledby="random69d45b23c726e18_label_6_19" tabindex="-1" aria-selected="false"><p class="tree_item branch" id="expandable_branch_30_211" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e18_label_6_19" href="https://cms.cis.k.hosei.ac.jp/course/section.php?id=211">第１回</a></p></li></ul></li></ul></li></ul></li></ul></li><li class="type_system depth_2 contains_branch" role="treeitem" aria-expanded="false" data-requires-ajax="true" data-loaded="false" data-node-id="expandable_branch_0_courses" data-node-key="courses" data-node-type="0" aria-labelledby="random69d45b23c726e3_label_2_20" tabindex="-1" aria-selected="false"><p class="tree_item branch" id="expandable_branch_0_courses" tabindex="-1"><a tabindex="-1" id="random69d45b23c726e3_label_2_20" href="https://cms.cis.k.hosei.ac.jp/course/index.php">コース</a></p></li></ul></li></ul>
            <div class="footer"></div>
            
        </div>

    </div>

</section>

  <span id="sb-1"></span><a href="#sb-2" class="visually-hidden-focusable">管理 をスキップする</a>

<section id="inst10" class=" block_settings block  card mb-3" role="navigation" data-block="settings" data-instance-id="10" aria-labelledby="instance-10-header">

    <div class="card-body p-3">

            <h3 id="instance-10-header" class="h5 card-title d-inline">管理</h3>


        <div class="card-text content mt-3">
            <div id="settingsnav" class="box py-3 block_tree_box"><ul class="block_tree list" role="tree" data-ajax-loader="block_navigation/site_admin_loader"><li class="type_course depth_1 contains_branch" tabindex="0" role="treeitem" aria-expanded="true" aria-owns="random69d45b23c726e24_group" aria-selected="true"><p class="tree_item root_node tree_item branch" tabindex="-1"><span tabindex="-1">コース管理</span></p><ul id="random69d45b23c726e24_group" role="group" tabindex="-1"><li class="type_setting depth_2 item_with_icon" tabindex="-1" role="treeitem" aria-selected="false"><p class="tree_item hasicon tree_item leaf" tabindex="-1"><a href="https://cms.cis.k.hosei.ac.jp/enrol/self/unenrolself.php?enrolid=28" tabindex="-1"><i class="icon fa fa-user fa-fw navicon" aria-hidden="true" tabindex="-1"></i>このコースから私を登録解除する</a></p></li></ul></li></ul></div>
            <div class="footer"></div>
            
        </div>

    </div>

</section>

  <span id="sb-2"></span></aside>
                </div>
            </div>

            <div class="columnright blockcolumn  has-blocks ">
                <div data-region="blocks-column" class="d-print-none">
                    <aside id="block-region-side-post" class="block-region" data-blockregion="side-post" data-droptarget="1" aria-labelledby="side-post-block-region-heading"><h2 class="visually-hidden" id="side-post-block-region-heading">補助ブロック</h2><a href="#sb-3" class="visually-hidden-focusable">フォーラムを検索する をスキップする</a>

<section id="inst43" class=" block_search_forums block  card mb-3" role="search" data-block="search_forums" data-instance-id="43" aria-labelledby="instance-43-header">

    <div class="card-body p-3">

            <h3 id="instance-43-header" class="h5 card-title d-inline">フォーラムを検索する</h3>


        <div class="card-text content mt-3">
            <div class="searchform">
    <div class="simplesearchform ">
        <form autocomplete="off" action="https://cms.cis.k.hosei.ac.jp/mod/forum/search.php?id=15" method="get" accept-charset="utf-8" class="mform d-flex flex-wrap align-items-center simplesearchform">
            <input type="hidden" name="id" value="15">
        <div class="input-group">
            <input type="text" id="searchinput-69d45b23cfb9e69d45b23c726e26" class="form-control" placeholder="検索" aria-label="検索" name="search" data-region="input" autocomplete="off" value="">
            <label for="searchinput-69d45b23cfb9e69d45b23c726e26">
                <span class="visually-hidden">検索</span>
            </label>
            <button type="submit" class="btn btn-submit  search-icon">
                <i class="icon fa fa-magnifying-glass fa-fw " aria-hidden="true"></i>
                <span class="visually-hidden">検索</span>
            </button>
    
        </div>
        </form>
    </div>    <div class="mt-3">
        <a href="https://cms.cis.k.hosei.ac.jp/mod/forum/search.php?id=15">高度な検索</a>
            <a class="btn btn-link p-0 me-2 icon-no-margin" role="button" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="right" data-bs-content="&lt;div class=&quot;no-overflow&quot;&gt;&lt;p&gt;テキスト中に存在する1つまたはそれ以上の言葉を検索する基本的な検索では空白で区切られた言葉を入力してください。半角2文字より大きな言葉が検索に使用されます。&lt;/p&gt;

&lt;p&gt;高度な検索では検索ボックス内に文字を入力せずに検索ボタンをクリックしてください。高度な検索フォームが表示されます。&lt;/p&gt;
&lt;/div&gt; " data-bs-html="true" tabindex="0" data-bs-trigger="focus" aria-label="ヘルプ">
              <i class="icon fa fa-circle-question text-info fa-fw " title="検索 のヘルプ" role="img" aria-label="検索 のヘルプ"></i>
            </a>
    </div>
</div>
            <div class="footer"></div>
            
        </div>

    </div>

</section>

  <span id="sb-3"></span><a href="#sb-4" class="visually-hidden-focusable">最新アナウンスメント をスキップする</a>

<section id="inst41" class=" block_news_items block  card mb-3" role="region" data-block="news_items" data-instance-id="41" aria-labelledby="instance-41-header">

    <div class="card-body p-3">

            <h3 id="instance-41-header" class="h5 card-title d-inline">最新アナウンスメント</h3>


        <div class="card-text content mt-3">
            (まだ新しいアナウンスメントは投稿されていません。)
            <div class="footer"></div>
            
        </div>

    </div>

</section>

  <span id="sb-4"></span><a href="#sb-5" class="visually-hidden-focusable">直近イベント をスキップする</a>

<section id="inst44" class=" block_calendar_upcoming block  card mb-3" role="region" data-block="calendar_upcoming" data-instance-id="44" aria-labelledby="instance-44-header">

    <div class="card-body p-3">

            <h3 id="instance-44-header" class="h5 card-title d-inline">直近イベント</h3>


        <div class="card-text content mt-3">
            <div id="calendar-upcoming-block-69d45b23e576169d45b23c726e27" data-template="core_calendar/upcoming_mini">
    <div class="card-text content calendarwrapper" id="month-upcoming-mini-69d45b23e576169d45b23c726e27" data-context-id="76" data-courseid="15" data-categoryid="7">
        <span class="overlay-icon-container hidden" data-region="overlay-icon-container">
            <span class="loading-icon icon-no-margin"><i class="icon fa fa-spinner fa-spin fa-fw " title="読み込み中" role="img" aria-label="読み込み中"></i></span>
        </span>
            <div class="event d-flex border-bottom pt-2 pb-3" data-eventtype-course="1" data-region="event-item">
                <div class="activityiconcontainer small courseicon me-2 assessment">
                        <img alt="未解答" title="未解答" src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/quiz/1775374816/monologo?filtericon=1" class="icon activityicon icon">
                </div>
                <div class="overflow-auto">
                    <h4 class="d-flex mb-1 h6">
                        <a class="text-truncate" data-type="event" data-action="view-event" data-event-id="136" href="https://cms.cis.k.hosei.ac.jp/calendar/view.php?view=day&amp;course=15&amp;time=1775613600#event_136" title="コース初回アンケート の受験可能期間の開始">コース初回アンケート の受験可能期間の開始</a>
                    </h4>
                    <div class="date small"><a href="https://cms.cis.k.hosei.ac.jp/calendar/view.php?view=day&amp;time=1775613600" title="2026年 04月 8日">
        <span class="date  " data-timestamp="1775613600" title="2026年 04月 8日">
            明日 04/8, 11:00
        </span>
    </a></div>
                </div>
            </div>
            <div class="event d-flex border-bottom pt-2 pb-3" data-eventtype-course="1" data-region="event-item">
                <div class="activityiconcontainer small courseicon me-2 assessment">
                        <img alt="ウィンドウを閉じる" title="ウィンドウを閉じる" src="https://cms.cis.k.hosei.ac.jp/theme/image.php/classic/quiz/1775374816/monologo?filtericon=1" class="icon activityicon icon">
                </div>
                <div class="overflow-auto">
                    <h4 class="d-flex mb-1 h6">
                        <a class="text-truncate" data-type="event" data-action="view-event" data-event-id="153" href="https://cms.cis.k.hosei.ac.jp/calendar/view.php?view=day&amp;course=15&amp;time=1776265140#event_153" title="コース初回アンケート の受験可能期間の終了">コース初回アンケート の受験可能期間の終了</a>
                    </h4>
                    <div class="date small"><a href="https://cms.cis.k.hosei.ac.jp/calendar/view.php?view=day&amp;time=1776265140" title="2026年 04月 15日">
        <span class="date  " data-timestamp="1776265140">
            2026年 04月 15日, 23:59
        </span>
    </a></div>
                </div>
            </div>
    </div>
</div>
            <div class="footer"><div class="gotocal"><a href="https://cms.cis.k.hosei.ac.jp/calendar/view.php?view=upcoming&amp;course=15">カレンダーへ移動する ...</a></div></div>
            
        </div>

    </div>

</section>

  <span id="sb-5"></span><a href="#sb-6" class="visually-hidden-focusable">最近の活動 をスキップする</a>

<section id="inst42" class=" block_recent_activity block  card mb-3" role="region" data-block="recent_activity" data-instance-id="42" aria-labelledby="instance-42-header">

    <div class="card-body p-3">

            <h3 id="instance-42-header" class="h5 card-title d-inline">最近の活動</h3>


        <div class="card-text content mt-3">
            <div class="activityhead">2026年 04月 5日(日曜日) 10:16 以来の活動</div><div class="activityhead mb-3"><a href="https://cms.cis.k.hosei.ac.jp/course/recent.php?id=15">最近の活動詳細 ...</a></div><h6>コース更新内容:</h6><p class="activity">ファイル を更新しました。<br><a href="https://cms.cis.k.hosei.ac.jp/mod/resource/view.php?id=290">教材</a></p><p class="activity">フォーラム を削除しました。</p><p class="activity">フォーラム を削除しました。</p><p class="activity">小テスト を更新しました。<br><a href="https://cms.cis.k.hosei.ac.jp/mod/quiz/view.php?id=291">コース初回アンケート</a></p>
            <div class="footer"></div>
            
        </div>

    </div>

</section>

  <span id="sb-6"></span></aside>
                </div>
            </div>
        </div>
    </div>
    
    <footer id="page-footer" class="footer-dark bg-dark text-light">
        <div class="container footer-dark-inner">
            <div id="course-footer"></div>
            <div class="pb-3">
            </div>
    
            <div class="logininfo">あなたは <a href="https://cms.cis.k.hosei.ac.jp/user/profile.php?id=326">霍 永豪</a> としてログインしています (<a href="https://cms.cis.k.hosei.ac.jp/login/logout.php?sesskey=7m7M1NdVAz">ログアウト</a>)</div>
            <div class="tool_usertours-resettourcontainer"></div>
            <div class="homelink"><a href="https://cms.cis.k.hosei.ac.jp/">Home</a></div>
            <nav class="nav navbar-nav d-md-none" aria-label="カスタムメニュー">
                    <ul class="list-unstyled pt-3">
                                        <li><a href="#" title="言語設定">日本語 &lrm;(ja)&lrm;</a></li>
                                    <li>
                                        <ul class="list-unstyled ms-3">
                                                            <li><a href="https://cms.cis.k.hosei.ac.jp/course/view.php?id=15&amp;lang=en" title="言語設定">English &lrm;(en)&lrm;</a></li>
                                                            <li><a href="https://cms.cis.k.hosei.ac.jp/course/view.php?id=15&amp;lang=ja" title="言語設定">日本語 &lrm;(ja)&lrm;</a></li>
                                        </ul>
                                    </li>
                    </ul>
            </nav>
            <div class="tool_dataprivacy"><a href="https://cms.cis.k.hosei.ac.jp/admin/tool/dataprivacy/summary.php">データ保持概要</a></div>
            
            <script>
//<![CDATA[
var require = {
    baseUrl : 'https://cms.cis.k.hosei.ac.jp/lib/requirejs.php/1775374816/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,
    waitSeconds : 0,

    paths: {
        jquery: 'https://cms.cis.k.hosei.ac.jp/lib/javascript.php/1775374816/lib/jquery/jquery-3.7.1.min',
        jqueryui: 'https://cms.cis.k.hosei.ac.jp/lib/javascript.php/1775374816/lib/jquery/ui-1.14.1/jquery-ui.min',
        jqueryprivate: 'https://cms.cis.k.hosei.ac.jp/lib/javascript.php/1775374816/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script src="https://cms.cis.k.hosei.ac.jp/lib/javascript.php/1775374816/lib/requirejs/require.min.js"></script>
<script>
//<![CDATA[
M.util.js_pending("core/first");
require(['core/first'], function() {
require(['core/prefetch'])
;
M.util.js_pending('filter_mathjaxloader/loader'); require(['filter_mathjaxloader/loader'], function(amd) {amd.configure({"mathjaxurl":"https:\/\/cdn.jsdelivr.net\/npm\/mathjax@3.2.2\/es5\/tex-mml-chtml.js","mathjaxconfig":"","lang":"ja"}); M.util.js_complete('filter_mathjaxloader/loader');});;
require(["media_videojs/loader"], function(loader) {
    loader.setUp('ja');
});;
M.util.js_pending('core_courseformat/courseeditor'); require(['core_courseformat/courseeditor'], function(amd) {amd.setViewFormat("15", {"editing":false,"supportscomponents":true,"statekey":"1775518992_1775520483","overriddenStrings":[]}); M.util.js_complete('core_courseformat/courseeditor');});;
M.util.js_pending('block_navigation/navblock'); require(['block_navigation/navblock'], function(amd) {amd.init("9"); M.util.js_complete('block_navigation/navblock');});;
M.util.js_pending('block_settings/settingsblock'); require(['block_settings/settingsblock'], function(amd) {amd.init("10", null); M.util.js_complete('block_settings/settingsblock');});;

require([
    'jquery',
    'core_calendar/selectors',
    'core_calendar/events',
], function(
    $,
    CalendarSelectors,
    CalendarEvents
) {
    var root = $('#month-upcoming-mini-69d45b23e576169d45b23c726e27');

    $('body').on(CalendarEvents.filterChanged, function(e, data) {
        M.util.js_pending("month-upcoming-mini-69d45b23e576169d45b23c726e27-filterChanged");

        // A filter value has been changed.
        // Find all matching cells in the popover data, and hide them.
        var target = $("#month-upcoming-mini-69d45b23e576169d45b23c726e27").find(CalendarSelectors.eventType[data.type]);

        var transitionPromise = $.Deferred();
        if (data.hidden) {
            transitionPromise.then(function() {
                return target.slideUp('fast').promise();
            });
        } else {
            transitionPromise.then(function() {
                return target.slideDown('fast').promise();
            });
        }

        transitionPromise.then(function() {
            M.util.js_complete("month-upcoming-mini-69d45b23e576169d45b23c726e27-filterChanged");

            return;
        });

        transitionPromise.resolve();
    });
});
;

require(['jquery', 'core_calendar/calendar_view'], function($, CalendarView) {
    CalendarView.init($("#calendar-upcoming-block-69d45b23e576169d45b23c726e27"), 'upcoming');
});
;

require(['jquery', 'core/custom_interaction_events'], function($, CustomEvents) {
    CustomEvents.define('#single_select69d45b23c726e30', [CustomEvents.events.accessibleChange]);
    $('#single_select69d45b23c726e30').on(CustomEvents.events.accessibleChange, function() {
        var ignore = $(this).find(':selected').attr('data-ignore');
        
    });
});
;

require(['jquery', 'message_popup/notification_popover_controller'], function($, Controller) {
    var container = $('#nav-notification-popover-container');
    var controller = new Controller(container);
    controller.registerEventListeners();
    controller.registerListNavigationEventListeners();
});
;

require(['jquery', 'core/custom_interaction_events'], function($, CustomEvents) {
    CustomEvents.define('#single_select69d45b23c726e43', [CustomEvents.events.accessibleChange]);
    $('#single_select69d45b23c726e43').on(CustomEvents.events.accessibleChange, function() {
        var ignore = $(this).find(':selected').attr('data-ignore');
        
    });
});
;

M.util.js_pending('theme_boost/loader');
require(['theme_boost/loader'], function() {
    M.util.js_complete('theme_boost/loader');
});
;
M.util.js_pending('format_topics/mutations'); require(['format_topics/mutations'], function(amd) {amd.init(); M.util.js_complete('format_topics/mutations');});;
M.util.js_pending('format_topics/section'); require(['format_topics/section'], function(amd) {amd.init(); M.util.js_complete('format_topics/section');});;

require(['core_course/manual_completion_toggle'], toggle => {
    toggle.init();
});
;

require(['core_course/manual_completion_toggle'], toggle => {
    toggle.init();
});
;

require(['core_course/manual_completion_toggle'], toggle => {
    toggle.init();
});
;

require(['core_course/manual_completion_toggle'], toggle => {
    toggle.init();
});
;

require(['core_course/manual_completion_toggle'], toggle => {
    toggle.init();
});
;

require(['core_courseformat/local/content'], function(component) {
    component.init(
        '#page', {}, null, null
    );
});
;
M.util.js_pending('core_course/view'); require(['core_course/view'], function(amd) {amd.init(); M.util.js_complete('core_course/view');});;
M.util.js_pending('core/notification'); require(['core/notification'], function(amd) {amd.init(76, []); M.util.js_complete('core/notification');});;
M.util.js_pending('core/log'); require(['core/log'], function(amd) {amd.setConfig({"level":"warn"}); M.util.js_complete('core/log');});;
M.util.js_pending('core/page_global'); require(['core/page_global'], function(amd) {amd.init(); M.util.js_complete('core/page_global');});;
M.util.js_pending('core/utility'); require(['core/utility'], function(amd) {M.util.js_complete('core/utility');});;
M.util.js_pending('core/storage_validation'); require(['core/storage_validation'], function(amd) {amd.init(1775520471); M.util.js_complete('core/storage_validation');});
    M.util.js_complete("core/first");
});
//]]>
</script>
<script>
//<![CDATA[
M.str = {"moodle":{"lastmodified":"\u6700\u7d42\u66f4\u65b0\u65e5\u6642","name":"\u540d\u79f0","error":"\u30a8\u30e9\u30fc","info":"\u60c5\u5831","yes":"Yes","no":"No","viewallcourses":"\u3059\u3079\u3066\u306e\u30b3\u30fc\u30b9\u3092\u8868\u793a\u3059\u308b","cancel":"\u30ad\u30e3\u30f3\u30bb\u30eb","confirm":"\u78ba\u8a8d","areyousure":"\u672c\u5f53\u306b\u3088\u308d\u3057\u3044\u3067\u3059\u304b?","closebuttontitle":"\u9589\u3058\u308b","unknownerror":"\u4e0d\u660e\u306a\u30a8\u30e9\u30fc","file":"\u30d5\u30a1\u30a4\u30eb","url":"URL","collapseall":"\u3059\u3079\u3066\u3092\u6298\u308a\u305f\u305f\u3080","expandall":"\u3059\u3079\u3066\u3092\u5c55\u958b\u3059\u308b"},"repository":{"type":"\u30bf\u30a4\u30d7","size":"\u30b5\u30a4\u30ba","invalidjson":"\u7121\u52b9\u306aJSON\u30b9\u30c8\u30ea\u30f3\u30b0\u3067\u3059\u3002","nofilesattached":"\u6dfb\u4ed8\u3055\u308c\u3066\u3044\u308b\u30d5\u30a1\u30a4\u30eb\u306f\u3042\u308a\u307e\u305b\u3093\u3002","filepicker":"\u30d5\u30a1\u30a4\u30eb\u30d4\u30c3\u30ab","logout":"\u30ed\u30b0\u30a2\u30a6\u30c8","nofilesavailable":"\u5229\u7528\u3067\u304d\u308b\u30d5\u30a1\u30a4\u30eb\u306f\u3042\u308a\u307e\u305b\u3093\u3002","norepositoriesavailable":"\u7533\u3057\u8a33\u3054\u3056\u3044\u307e\u305b\u3093\u3001\u73fe\u5728\u306e\u3042\u306a\u305f\u306e\u30ea\u30dd\u30b8\u30c8\u30ea\u3067\u306f\u6240\u8981\u306e\u30d5\u30a9\u30fc\u30de\u30c3\u30c8\u306e\u30d5\u30a1\u30a4\u30eb\u3092\u8fd4\u3059\u3053\u3068\u304c\u3067\u304d\u307e\u305b\u3093\u3002","fileexistsdialogheader":"\u30d5\u30a1\u30a4\u30eb\u767b\u9332\u6e08\u307f","fileexistsdialog_editor":"\u305d\u306e\u30d5\u30a1\u30a4\u30eb\u540d\u306e\u30d5\u30a1\u30a4\u30eb\u306f\u3042\u306a\u305f\u304c\u7de8\u96c6\u3057\u3066\u3044\u308b\u30c6\u30ad\u30b9\u30c8\u306b\u3059\u3067\u306b\u6dfb\u4ed8\u3055\u308c\u3066\u3044\u307e\u3059\u3002","fileexistsdialog_filemanager":"\u540c\u4e00\u30d5\u30a1\u30a4\u30eb\u540d\u306e\u30d5\u30a1\u30a4\u30eb\u304c\u3059\u3067\u306b\u6dfb\u4ed8\u3055\u308c\u3066\u3044\u307e\u3059\u3002","renameto":"\u30ea\u30cd\u30fc\u30e0 -> {$a}","referencesexist":"\u3053\u306e\u30d5\u30a1\u30a4\u30eb\u306b\u306f {$a} \u4ef6\u306e\u30ea\u30f3\u30af\u304c\u3042\u308a\u307e\u3059\u3002","select":"\u9078\u629e"},"admin":{"confirmdeletecomments":"\u672c\u5f53\u306b\u9078\u629e\u3057\u305f\u30b3\u30e1\u30f3\u30c8\u3092\u524a\u9664\u3057\u3066\u3082\u3088\u308d\u3057\u3044\u3067\u3059\u304b?","confirmation":"\u78ba\u8a8d"},"debug":{"debuginfo":"\u30c7\u30d0\u30c3\u30b0\u60c5\u5831","line":"\u884c","stacktrace":"\u30b9\u30bf\u30c3\u30af\u30c8\u30ec\u30fc\u30b9"},"langconfig":{"labelsep":":"}};
//]]>
</script>
<script>
//<![CDATA[
(function() {M.util.help_popups.setup(Y);
 M.util.js_pending('random69d45b23c726e45'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random69d45b23c726e45'); });
})();
//]]>
</script>

        </div>
    </footer>
</div><div id="yui3-css-stamp" style="position: absolute !important; visibility: hidden !important" class=""></div>


<deepl-input-controller translate="no"></deepl-input-controller><div></div></body></html>"""
    
    return '', html + help + cis_moodle, ''

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
