
controller = {
    init: function() {
        this.login = false;
        this.bindEvents();
    },

    bindEvents: function() {
        $(window).on("resize", this.onResize);

        $("#button-login").on("click", this.onLogin);

        $("#button-logout").on("click", this.onLogout);

        $("#menu-box").on("click", "button", this.onLeftMenu);
        
        $("#content-frame").on("load", this.onContentLoad);

        $(".panel-heading").on("click", this.onMenuPanel);
    },

    onResize: function(e) {
        controller.setFrameSize();
    },

    onLogin: function(e) {
        var username = $("#username").val();
        var password = $("#password").val();
        service.login(username, password, controller.loginSuccess, controller.loginFailed);
    },

    onLogout: function(e) {
        service.logout(controller.logoutSuccess, controller.logoutSuccess);
    },

    onLeftMenu: function(e) {
        var table = $(e.currentTarget).data("table");
        if (table) {
            controller.showTable(table);
        }
    },

    onMenuPanel: function(e) {
        if ($(this).find("span").hasClass("glyphicon-chevron-up")) {
            $(this).find("span").toggleClass("glyphicon-chevron-down");
            $(this).find("span").toggleClass("glyphicon-chevron-up");
        }
        else {
            $("#menu-box").find(".glyphicon-chevron-up")
                .removeClass("glyphicon-chevron-up")
                .addClass("glyphicon-chevron-down");
            $("#menu-box").find(".panel-collapse")
                .removeClass("in");

            $(this).find("span").toggleClass("glyphicon-chevron-down");
            $(this).find("span").toggleClass("glyphicon-chevron-up");
        }
    },

    onContentLoad: function(e) {
        controller.setFrameSize();
    },

    loginSuccess: function(data) {
        this.login = true;

        $("#username").val("");
        $("#password").val("");
        $("#login-message").text(" ");

        $("#login-view").hide();
        $("#editor-view").show();
    },

    loginFailed: function(code, message) {
        $("#login-message").text(message);
    },

    logoutSuccess: function(data) {
        this.login = false;
        $("#editor-view").hide();
        $("#login-view").show();
    },

    setFrameSize: function() {
	    var box = $("#content-box");
	    var frame = $(".content-frame:visible");
        if (frame.length == 0)  {
            return;
        }

        var win_width = $(window).innerWidth();
        var win_height = $(window).innerHeight();

        frame.innerWidth(win_width - 135);
        frame.height(0);
            
        var frame_body = frame[0].contentWindow.document.body;
        var frame_height = frame_body.scrollHeight + 1;
        
        if (frame_height > win_height) {
		    frame.height(frame_height);
	    }
	    else {
		    frame.height(win_height);
	    }
    },

    showTable: function(table_name) {
        var url = "common_table.html?table=" + table_name;
        $("#table-frame").attr("src", url);
 
        $("#editor-frame").hide();
        $("#table-frame").show();
        this.setFrameSize();
    },

    showTableView: function() {
        $("#editor-frame").hide();
        $("#table-frame").show();
    },

    editRecord: function(table_name, record_id) {
        var url = "editor.html?table=" + table_name + "&record=" + record_id;
        $("#editor-frame").attr("src", url);

        $("#table-frame").hide();
        $("#editor-frame").show();
        this.setFrameSize();
    },
}

$(document).ready(function() {
    controller.init();
});

