from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteraction:

    class TestSortablePage:

        def test_sortable(self,driver):
            sortable_page = SortablePage(driver,'https://demoqa.com/sortable')
            sortable_page.open()
            list_before,list_after =  sortable_page.change_list_order()
            grid_before,grid_after = sortable_page.change_grid_order()
            assert list_before != list_after
            assert grid_before != grid_after

    class TestSelectPage:
        def test_selectable(self,driver):
            selectable_page = SelectablePage(driver,'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, 'no elements were selected'
            assert len(item_grid) > 0, "no elements were selected"

    class TestResizablePage:

        def test_resizable_page(self,driver):
            resizable_page = ResizablePage(driver,'https://demoqa.com/resizable')
            resizable_page.open()
            max_box,min_box = resizable_page.change_size_resizable_box()
            max_resize,min_resize = resizable_page.change_size_resizable()
            assert('500px','380px') == max_box, "maximum size not equal to 500px"
            assert('150px','150px') == min_box, "maximum size not equal to 150px"
            assert min_resize != max_resize,"resizable has not been changed"