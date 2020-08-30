package com.qw.springCloudClientAccount.modules.account.service.Impl;

import com.qw.springCloudClientAccount.modules.account.dao.UserDao;
import com.qw.springCloudClientAccount.modules.account.pojo.City;
import com.qw.springCloudClientAccount.modules.account.pojo.User;
import com.qw.springCloudClientAccount.modules.account.service.TestFeignClient;
import com.qw.springCloudClientAccount.modules.account.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.ResourceUtils;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

/**
 * ClassName: UserServiceImpl <br/>
 * Description: <br/>
 * date: 2020/8/20 13:36<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserDao userDao;
    /*@Autowired
    private RestTemplate restTemplate;*/

    /**
     * 当 TestFeignClient 有了实现类后，在注入时，idea 会报错
     * Could not autowire. There is more than one bean of 'xxx' type
     *意思是注入的 bean 类型不止一个，这并不影响项目运行，相当于一个警告
     * 解决方案：
     *1、给不同的实现标注名字，此处使用 Qulifier 注解标注，根据 bean 名称注入
     *2、在需要指定的类型处添加 @Primary 注解；
     */
    @Autowired
    private TestFeignClient testFeignClient;

    /**
     * 查询
     * 引入 Feign 后，不再使用 RestTemplate 调用远程接口，交给 FeignClient
     */
    @Override
    public User getUserByUserId(int userId) {
        User user = userDao.getUserByUserId(userId);
        List<City> cities = testFeignClient.getCitiesByCountryId(522);
        /*List<City> cities = Optional.ofNullable(restTemplate.getForObject(
                "http://CLIENT-TEST/api/cities/{countryId}", List.class,522))
                .orElse(Collections.emptyList());*/
        user.setCities(cities);
        return user;
    }

}
