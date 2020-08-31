package com.qw.springCloudClientAccount.modules.account.service;

import com.qw.springCloudClientAccount.modules.account.pojo.City;
import com.qw.springCloudClientAccount.modules.account.service.Impl.TestFeignClientFallBack;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.context.annotation.Primary;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

/**
 * ClassName: TestFeignClient <br/>
 * Description: <br/>
 * date: 2020/8/30 15:47<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 * 指定生产者服务注册名
 */
@FeignClient(value = "SC-CLIENT-TEST", fallback = TestFeignClientFallBack.class)
@Primary
public interface TestFeignClient {
    /**
     * 此处整合了 Spring MVC 的用法，使用 Restful 方式调用
     */
    @GetMapping("/api/cities/{countryId}")
    List<City> getCitiesByCountryId(@PathVariable int countryId);

}
