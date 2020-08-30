package com.qw.springcloudregister.cogfig;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;

/**
 * ClassName: WebSecurityConfig <br/>
 * Description: <br/>
 * date: 2020/8/28 16:43<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 * 给注册中心 配置需要用户名和密码认证（basic认证）
 */
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        //Basic 认证是一种较为简单的 http 认证方式
        http.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.NEVER);
        http.csrf().disable();
        http.authorizeRequests().anyRequest().authenticated().and().httpBasic();
    }
}
