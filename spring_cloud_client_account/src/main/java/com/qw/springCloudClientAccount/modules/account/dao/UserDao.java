package com.qw.springCloudClientAccount.modules.account.dao;

import com.qw.springCloudClientAccount.modules.account.pojo.User;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * ClassName: UserDao <br/>
 * Description: <br/>
 * date: 2020/8/20 8:57<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
@Repository
@Mapper
public interface UserDao {

    //查询
    @Select("select * from user where user_id = #{userId}")
    User getUserByUserId(int userId);

}
