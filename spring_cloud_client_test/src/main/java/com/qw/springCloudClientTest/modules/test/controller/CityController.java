package com.qw.springCloudClientTest.modules.test.controller;

import com.qw.springCloudClientTest.modules.test.pojo.City;
import com.qw.springCloudClientTest.modules.test.service.CityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

/**
 * ClassName: CityController <br/>
 * Description: <br/>
 * date: 2020/8/11 19:59<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
@RestController
@RequestMapping("/api")
public class CityController {

    @Autowired
    private CityService cityService;

    /**
     * 127.0.0.1:8761/api/cities/522 ---- get
     * 通过id查询
     * @PathVariable 获取路径参数
     */
    @GetMapping("/cities/{countryId}")
    public List<City> getCitiesByCountryId(@PathVariable int countryId){
        return cityService.getCitiesByCountryId(countryId);
    }

}
