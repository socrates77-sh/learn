var json_parse = (function () {

// This is a function that can parse a JSON text, producing a JavaScript
// data structure. It is a simple, recursive descent parser. It does not use
// eval or regular expressions, so it can be used as a model for implementing
// a JSON parser in other languages.

// We are defining the function inside of another function to avoid creating
// global variables.

    var at,     // The index of the current character
        ch,     // The current character
        escapee = {
            '"':  '"',
            '\\': '\\',
            '/':  '/',
            b:    '\b',
            f:    '\f',
            n:    '\n',
            r:    '\r',
            t:    '\t'
        },
        text,

        error = function (m) {

// Call error when something is wrong.

            throw {
                name:    'SyntaxError',
                message: m,
                at:      at,
                text:    text
            };
        },

        next = function (c) {

// If a c parameter is provided, verify that it matches the current character.

            if (c && c !== ch) {
                error("Expected '" + c + "' instead of '" + ch + "'");
            }

// Get the next character. When there are no more characters,
// return the empty string.

            ch = text.charAt(at);
            at += 1;
            return ch;
        },

        number = function () {

// Parse a number value.

            var number,
                string = '';

            if (ch === '-') {
                string = '-';
                next('-');
            }
            while (ch >= '0' && ch <= '9') {
                string += ch;
                next();
            }
            if (ch === '.') {
                string += '.';
                while (next() && ch >= '0' && ch <= '9') {
                    string += ch;
                }
            }
            if (ch === 'e' || ch === 'E') {
                string += ch;
                next();
                if (ch === '-' || ch === '+') {
                    string += ch;
                    next();
                }
                while (ch >= '0' && ch <= '9') {
                    string += ch;
                    next();
                }
            }
            number = +string;
            if (isNaN(number)) {
                error("Bad number");
            } else {
                return number;
            }
        },

        string = function () {

// Parse a string value.

            var hex,
                i,
                string = '',
                uffff;

// When parsing for string values, we must look for " and \ characters.

            if (ch === '"') {
                while (next()) {
                    if (ch === '"') {
                        next();
                        return string;
                    } else if (ch === '\\') {
                        next();
                        if (ch === 'u') {
                            uffff = 0;
                            for (i = 0; i < 4; i += 1) {
                                hex = parseInt(next(), 16);
                                if (!isFinite(hex)) {
                                    break;
                                }
                                uffff = uffff * 16 + hex;
                            }
                            string += String.fromCharCode(uffff);
                        } else if (typeof escapee[ch] === 'string') {
                            string += escapee[ch];
                        } else {
                            break;
                        }
                    } else {
                        string += ch;
                    }
                }
            }
            error("Bad string");
        },

        white = function () {

// Skip whitespace.

            while (ch && ch <= ' ') {
                next();
            }
        },

        word = function () {

// true, false, or null.

            switch (ch) {
            case 't':
                next('t');
                next('r');
                next('u');
                next('e');
                return true;
            case 'f':
                next('f');
                next('a');
                next('l');
                next('s');
                next('e');
                return false;
            case 'n':
                next('n');
                next('u');
                next('l');
                next('l');
                return null;
            }
            error("Unexpected '" + ch + "'");
        },

        value,  // Place holder for the value function.

        array = function () {

// Parse an array value.

            var array = [];

            if (ch === '[') {
                next('[');
                white();
                if (ch === ']') {
                    next(']');
                    return array;   // empty array
                }
                while (ch) {
                    array.push(value());
                    white();
                    if (ch === ']') {
                        next(']');
                        return array;
                    }
                    next(',');
                    white();
                }
            }
            error("Bad array");
        },

        object = function () {

// Parse an object value.

            var key,
                object = {};

            if (ch === '{') {
                next('{');
                white();
                if (ch === '}') {
                    next('}');
                    return object;   // empty object
                }
                while (ch) {
                    key = string();
                    white();
                    next(':');
                    if (Object.hasOwnProperty.call(object, key)) {
                        error('Duplicate key "' + key + '"');
                    }
                    object[key] = value();
                    white();
                    if (ch === '}') {
                        next('}');
                        return object;
                    }
                    next(',');
                    white();
                }
            }
            error("Bad object");
        };

    value = function () {

// Parse a JSON value. It could be an object, an array, a string, a number,
// or a word.

        white();
        switch (ch) {
        case '{':
            return object();
        case '[':
            return array();
        case '"':
            return string();
        case '-':
            return number();
        default:
            return ch >= '0' && ch <= '9' ? number() : word();
        }
    };

// Return the json_parse function. It will have access to all of the above
// functions and variables.

    return function (source, reviver) {
        var result;

        text = source;
        at = 0;
        ch = ' ';
        result = value();
        white();
        if (ch) {
            error("Syntax error");
        }

// If there is a reviver function, we recursively walk the new structure,
// passing each name/value pair to the reviver function for possible
// transformation, starting with a temporary root object that holds the result
// in an empty key. If there is not a reviver function, we simply return the
// result.

        return typeof reviver === 'function' ? (function walk(holder, key) {
            var k, v, value = holder[key];
            if (value && typeof value === 'object') {
                for (k in value) {
                    if (Object.hasOwnProperty.call(value, k)) {
                        v = walk(value, k);
                        if (v !== undefined) {
                            value[k] = v;
                        } else {
                            delete value[k];
                        }
                    }
                }
            }
            return reviver.call(holder, key, value);
        }({'': result}, '')) : result;
    };
}());

String.prototype.trim = function () {
    return this.replace(/^\s*/, "").replace(/\s*$/, "");
}

function load_comments()
{
    $.post(
        "/pydoc.py",
        {
            "action":"load_comments",
            "key":$("#ui-dialog-title-comment_block").text()
        },
        function(html){
            $("#comment_list").html( html );
        }
    );
}
function clear_comments()
{
    $("#comment_list").html("载入中...");
}

function comment_link_clicked()
{
    var title;

    if($(this).parent("li").size() == 0){
        title = $(this).parent().text().trim();
        title = title.substring(0, title.length - 1);
        if(title.indexOf("　") > 0)
        {
            title = title.slice(title.indexOf("　")+1);
        }
    }
    else
        title = $(this).next().text().trim();

    var tmp = document.location.pathname.split("/");
    var filename = tmp[tmp.length - 1];

    var key = filename + "/" + title;

    $("#ui-dialog-title-comment_block").text(key);    

    $('#comment_block')
        .attr('title', key)
/*
        .dialog({
            autoOpen: false,
            width: 600,
            height: 500,
            title: key,
            open: load_comments,
            close: clear_comments
        }) 
*/
        .dialog('open');
    return false;
}

function add_comment_icon()
{
    $("div.body")
        .find("h1,h2,h3,h4")
        .append('<img src="_static/comment.png" class="comment_link"/>');

    $("div.sphinxsidebarwrapper ul a.reference")
        .before('<img src="_static/comment.png" class="comment_link"/>');

    $("img.comment_link")
        .click( comment_link_clicked );        
}
function send_comment()
{
    $.post(
        "/pydoc.py", 
        {
            "action":"add_comment",
            "key":$("#ui-dialog-title-comment_block").text(),
            "name":$("#comment_name").val(),
            "comment":$("#comment_text").val()
        },
        function(html){
            load_comments();
            $("#comment_text").val("");
        }
    );
}

function add_comment_block()
{
    $("body").append('<div id="comment_block">评论人：<input type="text" id="comment_name"/><input type="button" id="comment_send" value="发送"/><br/><textarea style="width:95%;" id="comment_text" rows="4"></textarea><div id="comment_list"></div></div>');

    $("#comment_send").click( send_comment );
}

jQuery.cookie = function(name, value, options) { 
    if (typeof value != 'undefined') { // name and value given, set cookie 
        options = options || {}; 
        if (value === null) { 
            value = ''; 
            options.expires = -1; 
        } 
        var expires = ''; 
        if (options.expires && (typeof options.expires == 'number' || options.expires.toUTCString)) { 
            var date; 
            if (typeof options.expires == 'number') { 
                date = new Date(); 
                date.setTime(date.getTime() + (options.expires * 24 * 60 * 60 * 1000)); 
            } else { 
                date = options.expires; 
            } 
            expires = '; expires=' + date.toUTCString(); // use expires attribute, max-age is not supported by IE 
        } 
        var path = options.path ? '; path=' + options.path : ''; 
        var domain = options.domain ? '; domain=' + options.domain : ''; 
        var secure = options.secure ? '; secure' : ''; 
        document.cookie = [name, '=', encodeURIComponent(value), expires, path, domain, secure].join(''); 
    } else { // only name given, get cookie 
        var cookieValue = null; 
        if (document.cookie && document.cookie != '') { 
            var cookies = document.cookie.split(';'); 
            for (var i = 0; i < cookies.length; i++) { 
                var cookie = jQuery.trim(cookies[i]); 
                // Does this cookie string begin with the name we want? 
                if (cookie.substring(0, name.length + 1) == (name + '=')) { 
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break; 
                } 
            } 
        } 
        return cookieValue; 
    } 
};

hide_sidebar = function(){
    $("div.bodywrapper").css("margin-left", "0px");
    $("div.sphinxsidebar").hide();
};

show_sidebar = function(){
    $("div.bodywrapper").css("margin-left", "300px");
    $("div.sphinxsidebar").show();            
}

var numbers;

function add_head_number(tag, key)
{
    $(tag).each(function(){
        var text = $(this).text().slice(0,-1).trim();
        if(numbers[key][text]) $(this).prepend(numbers[key][text] + "　");
    });
}

function add_figure_number(key)
{
    $("div.figure p.caption").each(function(){
        var text = $(this).text().trim();
        if(numbers[key][text]) $(this).prepend('<span class="fignumber" style="font-weight:bold">图' + numbers[key][text] + '</span>' + " ");
    });
    $("a[href^=#fig-]").each(function(){
        var div = $($(this).attr("href"));
        var text = div.find("span.fignumber").text();
        if(text) $(this).text(text).css("font-weight","bold");
    });
}

$(document).ready(
    function(){
        add_comment_icon();
        add_comment_block();

        $('#comment_block')
            .dialog({
                autoOpen: false,
                width: 600,
                height: 500,
                open: load_comments,
                close: clear_comments
            }); 
            
        //$("#searchbox").hide();

        clear_comments();
        $("a#toggle_sidebar").toggle(
            function(){
                hide_sidebar();
                $.cookie("hide_sidebar","1"); 
                return false;
            },
            function(){
                show_sidebar();
                $.cookie("hide_sidebar", "", {expires:-1});          
                return false;
            }
        );

        $(window).keydown(function(event){
            if(event.altKey && event.keyCode == 88) $("a#toggle_sidebar").click();
        });

        if($.cookie("hide_sidebar")) hide_sidebar();
        
        $("p[id^=sec-]").each(function(){
            var id = $(this).attr("id");
            $(this).removeAttr("id");
            $(this).prev().attr("id", id);
        });
        
        $("img").css("cursor","pointer").toggle(
            function(){
                $(this).attr("imagewidth", $(this).css("width"));
                $(this).css("width","");
            },
            function(){
                $(this).css("width",$(this).attr("imagewidth"));
            }
        );
        
        $.getJSON("numbers.json", {}, function(data){
            numbers = data;
            
            add_head_number("h1", "chapters");
            add_head_number("h2", "sections");
            add_head_number("h3", "subsections");
            add_figure_number("figures");
            
            
        });
        
    }
);
