package com.qw.springCloudClientAccount.modules.account.controller;

import com.qw.springCloudClientAccount.modules.account.pojo.User;
import com.qw.springCloudClientAccount.modules.account.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.awt.*;
import java.io.File;
import java.io.IOException;

/**
 * ClassName: UserController <br/>
 * Description: <br/>
 * date: 2020/8/20 13:32<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
@RestController
@RequestMapping("/api")
public class UserController {

    @Autowired
    private UserService userService;

    /**
     * 127.0.0.1:8762/api/user/1 ---- get
     * 查询
     */
    @GetMapping("/user/{userId}")
    public User getUserByUserId(@PathVariable int userId){
        return userService.getUserByUserId(userId);
    }


}
