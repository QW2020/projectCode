package com.qw.springCloudClientAccount.modules.account.service.Impl;

import com.qw.springCloudClientAccount.modules.account.pojo.City;
import com.qw.springCloudClientAccount.modules.account.service.TestFeignClient;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

/**
 * ClassName: TestFeignClientFallBack <br/>
 * Description: <br/>
 * date: 2020/8/30 16:19<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
@Component
public class TestFeignClientFallBack implements TestFeignClient {

    @Override
    public List<City> getCitiesByCountryId(int countryId) {
        return new ArrayList<City>();
    }
}
