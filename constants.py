import os
from flask import request

LEARNPYTHON_DOMAIN = "www.learnpython.org"
LEARNJAVA_DOMAIN = "www.learnjavaonline.org"
LEARNC_DOMAIN = "www.learn-c.org"
LEARNJS_DOMAIN = "www.learn-js.org"
LEARNRUBY_DOMAIN = "www.learnrubyonline.org"
LEARNSHELL_DOMAIN = "www.learnshell.org"
LEARNPHP_DOMAIN = "www.learn-php.org"
LEARNPERL_DOMAIN = "www.learn-perl.org"

DOMAIN_DATA = {
	LEARNPYTHON_DOMAIN : {
		"language" : "python",
		"analytics" : "UA-22741967-1",
        "namespace" : "learnpython.org",
		"full_url" : "http://www.learnpython.org",
		"sender" : "LearnPython.org <admin@learnpython.org>",
		"styled_domain" : "LearnPython.org",
		"contact_email" : "admin@learnpython.org",
		"support_email" : "support@learnpython.org",
		"logo" : "/static/img/learnpython.png",
		"jobs_logo" : "/static/img/learnpython-jobs.png",
		"language_uppercase" : "Python",
		"twitter" : "@learnpython",
        "favicon" : "favicon-learnpython.ico",
		"copyright" : "Copyright &copy; LearnPython.org.",
		"default_code" : """# Welcome to the Interactive Python Tutorial.
# Start by choosing a chapter and
# write your code in this window.

print "Hello, World!"
"""
	},
	LEARNC_DOMAIN : {
		"language" : "c",
		"analytics" : "UA-22741967-3",
        "namespace" : "learn-c.org",
		"full_url" : "http://www.learn-c.org",
		"sender" : "Learn-C.org <admin@learn-c.org>",
		"styled_domain" : "Learn-C.org",
		"contact_email" : "admin@learn-c.org",
		"support_email" : "support@learn-c.org",
		"logo" : "/static/img/learn-c.png",
		"jobs_logo" : "/static/img/learn-c-jobs.png",
		"language_uppercase" : "C",
		"twitter" : "@learnc",
        "favicon" : "favicon-learn-c.ico",
		"copyright" : "Copyright &copy; Learn-C.org. ",
		"default_code" : """/* Welcome to the Interactive C Tutorial.
Start by choosing a chapter and
write your code in this window. */

#include <stdio.h>

int main() {
  printf("Hello, World!");
  return 0;
}
"""
	},
	LEARNJAVA_DOMAIN : {
		"language" : "java",
		"analytics" : "UA-22741967-4",
        "namespace" : "learnjavaonline.org",
		"full_url" : "http://www.learnjavaonline.org",
		"sender" : "LearnJavaOnline.org <admin@learnjavaonline.org>",
		"styled_domain" : "LearnJavaOnline.org",
		"contact_email" : "admin@learnjavaonline.org",
		"support_email" : "support@learnjavaonline.org",
		"logo" : "/static/img/learnjavaonline.png",
		"jobs_logo" : "/static/img/learnjavaonline-jobs.png",
		"language_uppercase" : "Java",
		"twitter" : "@learnjava",
        "favicon" : "favicon-learnjava.ico",
		"copyright" : "Copyright &copy; LearnJavaOnline.org.",
		"default_code" : """// Welcome to the Interactive Java Tutorial.
// Start by choosing a chapter and
// write your code in this window.

public class Main {

  public static void main(String[] args) {

    System.out.println("Hello, World!");

  }

}
"""

	},
	LEARNJS_DOMAIN : {
		"language" : "javascript",
		"analytics" : "UA-22741967-5",
        "namespace" : "learn-js.org",
		"full_url" : "http://www.learn-js.org",
		"sender" : "Learn-JS.org <admin@learn-js.org>",
		"styled_domain" : "Learn-JS.org",
		"contact_email" : "admin@learn-js.org",
		"support_email" : "support@learn-js.org",
		"logo" : "/static/img/learn-js.png",
		"jobs_logo" : "/static/img/learn-js-jobs.png",
		"language_uppercase" : "JavaScript",
		"twitter" : "@learnjs",
        "favicon" : "favicon-learn-js.ico",
		"copyright" : "Copyright &copy; Learn-JS.org.",
		"default_code" : """// Welcome to the Interactive JavaScript Tutorial.
// Start by choosing a chapter and
// write your code in this window.

console.log("Hello, World!");
"""
	},
    LEARNRUBY_DOMAIN : {
		"language" : "ruby",
		"analytics" : "UA-22741967-6",
        "namespace" : "learnrubyonline.org",
		"full_url" : "http://www.learnrubyonline.org",
		"sender" : "Learn-JS.org <admin@learnrubyonline.org>",
		"styled_domain" : "LearnRubyOnline.org",
		"contact_email" : "admin@learnrubyonline.org",
		"support_email" : "support@learnrubyonline.org",
		"logo" : "/static/img/learnrubyonline.png",
		"jobs_logo" : "/static/img/learnrubyonline-jobs.png",
		"language_uppercase" : "Ruby",
		"twitter" : "@learnruby",
        "favicon" : "favicon-ruby.ico",
		"copyright" : "Copyright &copy; LearnRubyOnline.org.",
		"default_code" : """# Welcome to the Interactive Ruby Tutorial.
# Start by choosing a chapter and
# write your code in this window.

puts 'Hello, World!'
"""
	},
    LEARNSHELL_DOMAIN : {
		"language" : "bash",
		"analytics" : "UA-22741967-7",
        "namespace" : "learnshell.org",
		"full_url" : "http://www.learnshell.org",
		"sender" : "LearnShell.org <admin@learnshell.org>",
		"styled_domain" : "LearnShell.org",
		"contact_email" : "admin@learnshell.org",
		"support_email" : "support@learnshell.org",
		"logo" : "/static/img/learnshell.png",
		"jobs_logo" : "/static/img/learnshell-jobs.png",
		"language_uppercase" : "Shell Programming",
		"twitter" : "@learnshell",
        "favicon" : "favicon-shell.ico",
		"copyright" : "Copyright &copy; LearnShell.org.",
		"default_code" : """#!/bin/bash
# Welcome to the Interactive Shell Tutorial.
# Start by choosing a chapter and
# write your code in this window.

echo "Hello, World!";
"""
	},

    LEARNPHP_DOMAIN : {
		"language" : "php",
		"analytics" : "UA-22741967-7",
        "namespace" : "learn-php.org",
		"full_url" : "http://www.learn-php.org",
		"sender" : "Learn-PHP.org <admin@learn-php.org>",
		"styled_domain" : "Learn-PHP.org",
		"contact_email" : "admin@learn-php.org",
		"support_email" : "support@learn-php.org",
		"logo" : "/static/img/learn-php.png",
		"jobs_logo" : "/static/img/learn-php-jobs.png",
		"language_uppercase" : "PHP",
		"twitter" : "@learnphp",
        "favicon" : "favicon-learn-php.ico",
		"copyright" : "Copyright &copy; Learn-PHP.org.",
		"default_code" : """<?php
// Welcome to the Interactive PHP Tutorial.
// Start by choosing a chapter and
// write your code in this window.

print('Hello, World!');
?>
"""},

    LEARNPERL_DOMAIN : {
		"language" : "perl",
		"analytics" : "UA-22741967-8",
        "namespace" : "learn-perl.org",
		"full_url" : "http://www.learn-perl.org",
		"sender" : "Learn-Perl.org <admin@learn-perl.org>",
		"styled_domain" : "Learn-Perl.org",
		"contact_email" : "admin@learn-perl.org",
		"support_email" : "support@learn-perl.org",
		"logo" : "/static/img/learn-perl.png",
		"jobs_logo" : "/static/img/learn-perl-jobs.png",
		"language_uppercase" : "Perl",
		"twitter" : "@learnperl",
        "favicon" : "favicon-learn-perl.ico",
		"copyright" : "Copyright &copy; Learn-Perl.org.",
		"default_code" : """# Welcome to the Interactive Perl Tutorial.
# Start by choosing a chapter and write your code in this window.

echo 'Hello, World!';
"""},

}