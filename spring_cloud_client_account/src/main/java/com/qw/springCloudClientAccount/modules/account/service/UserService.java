package com.qw.springCloudClientAccount.modules.account.service;

import com.qw.springCloudClientAccount.modules.account.pojo.User;
import com.qw.springCloudClientAccount.modules.common.vo.Result;
import org.springframework.web.multipart.MultipartFile;

/**
 * ClassName: UserService <br/>
 * Description: <br/>
 * date: 2020/8/20 13:36<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
public interface UserService {

    User getUserByUserId(int userId);

}
