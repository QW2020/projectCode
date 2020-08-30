package com.qw.springCloudClientTest.modules.test.service;

import com.qw.springCloudClientTest.modules.test.pojo.City;

import java.util.List;

/**
 * ClassName: CityService <br/>
 * Description: <br/>
 * date: 2020/8/11 21:47<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
public interface CityService {
    List<City> getCitiesByCountryId(int countryId);

}
