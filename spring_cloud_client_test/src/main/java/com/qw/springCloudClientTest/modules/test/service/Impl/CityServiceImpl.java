package com.qw.springCloudClientTest.modules.test.service.Impl;

import com.qw.springCloudClientTest.modules.test.dao.CityDao;
import com.qw.springCloudClientTest.modules.test.pojo.City;
import com.qw.springCloudClientTest.modules.test.service.CityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.Optional;

/**
 * ClassName: CityServiceImpl <br/>
 * Description: <br/>
 * date: 2020/8/11 21:47<br/>
 *
 * @author Acer-pc<br/>
 * @since JDK 1.8
 */
@Service
public class CityServiceImpl implements CityService {

    @Autowired
    private CityDao cityDao;

    //根据id查询
    @Override
    public List<City> getCitiesByCountryId(int countryId) {
//        return cityDao.getCitiesByCountryId(countryId);
        return Optional.ofNullable(cityDao.getCitiesByCountryId(countryId))
                .orElse(Collections.emptyList());
    }
}
