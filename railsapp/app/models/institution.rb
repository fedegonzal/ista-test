class Institution < ApplicationRecord
    def self.all(col="id", dir="asc")
        find_by_sql("
        SELECT id, source, university, country, 
        json_extract(location, '$.lat') as lat,
        json_extract(location, '$.lng') as lng
        FROM institutions
        ORDER BY #{col} #{dir}
        ")
    end    
end
